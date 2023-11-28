import unittest
from GUI import utils
from datetime import datetime
from Controller import antibiotic_controller, bill_controler, client_controler, fertilizer_controller, pest_controller
from Model import Antibioticos, ControlFertilizantes, ControlPlagas, Cliente, Factura


class Test_Program(unittest.TestCase):

    def setUp(self):
        self.antibiotic_1 = antibiotic_controller.AntibioticController.create(name="antibiotic_1", dose="10ml",
                                                                              animal_type="bovino", value=12000)
        self.antibiotic_2 = antibiotic_controller.AntibioticController.create(name="antibiotic_2", dose="60ml",
                                                                              animal_type="caprino", value=50000)
        self.fertilizer_1 = fertilizer_controller.FertilizerController.create(name="fertilizer_1", ica="ABC123",
                                                                              freq="2 días", value=500000,
                                                                              last_applic="4/10/2023")
        self.fertilizer_2 = fertilizer_controller.FertilizerController.create(name="fertilizer_2", ica="DEF456",
                                                                              freq="6 días", value=500000,
                                                                              last_applic="22/9/2024")
        self.pest_control_1 = pest_controller.PestController.create(name="pest_1", ica="GHI789", freq="8 días",
                                                                    value=120000, grace_period="15")
        self.pest_control_2 = pest_controller.PestController.create(name="pest_2", ica="JKL963", freq="2 días",
                                                                    value=101000, grace_period="7")
        self.client_1 = client_controler.ClientControler.create(name="Sebastian Cacante", dni="1091272102")
        self.client_2 = client_controler.ClientControler.create(name="Juan Esteban Cardona", dni="70302593")
        self.bill_1 = bill_controler.BillControler.create()
        self.bill_2 = bill_controler.BillControler.create()
        bill_controler.BillControler.append_product(bill=self.bill_1, products=[self.antibiotic_1, self.fertilizer_1,
                                                                                self.pest_control_1])
        bill_controler.BillControler.append_product(bill=self.bill_2, products=[self.antibiotic_2, self.fertilizer_2,
                                                                                self.pest_control_2])
        client_controler.ClientControler.append_bill(bill=self.bill_1, client=self.client_1)
        client_controler.ClientControler.append_bill(bill=self.bill_2, client=self.client_2)

    def test_search(self):
        self.assertIsInstance(bill_controler.BillControler.search(date=self.bill_1.date,
                                                                  bills=self.client_1.bills), Factura.Factura)
        self.assertIsInstance(bill_controler.BillControler.search(date=self.bill_2.date,
                                                                  bills=self.client_2.bills), Factura.Factura)
        self.assertFalse(bill_controler.BillControler.search(date="1/1/2018",
                                                             bills=self.client_1.bills), Factura.Factura)
        self.assertFalse(bill_controler.BillControler.search(date="3/10/2010",
                                                             bills=self.client_2.bills), Factura.Factura)
        self.assertIsInstance(client_controler.ClientControler.search(dni="1091272102"), Cliente.Cliente)
        self.assertIsInstance(client_controler.ClientControler.search(dni="70302593"), Cliente.Cliente)
        self.assertFalse(client_controler.ClientControler.search(dni="9999999999"), Cliente.Cliente)

    def test_instances(self):
        self.assertIsInstance(self.antibiotic_1, Antibioticos.Antibioticos)
        self.assertIsInstance(self.antibiotic_2, Antibioticos.Antibioticos)
        self.assertIsInstance(self.pest_control_1, ControlPlagas.ControlPlagas)
        self.assertIsInstance(self.pest_control_2, ControlPlagas.ControlPlagas)
        self.assertIsInstance(self.fertilizer_1, ControlFertilizantes.ControlFertilizantes)
        self.assertIsInstance(self.fertilizer_2, ControlFertilizantes.ControlFertilizantes)
        self.assertIsInstance(self.bill_1, Factura.Factura)
        self.assertIsInstance(self.bill_2, Factura.Factura)
        self.assertIsInstance(self.client_1, Cliente.Cliente)
        self.assertIsInstance(self.client_2, Cliente.Cliente)

    def test_input_validation(self):
        self.assertTrue(utils.validate_name("Sebastian"))
        self.assertTrue(utils.validate_name("Sebastian Cacante"))
        self.assertTrue(utils.validate_name("Sebastian Cacante Salazar"))
        self.assertTrue(utils.validate_name("Mañe"))
        self.assertFalse(utils.validate_name("$eb?stian"))
        self.assertFalse(utils.validate_name("Se"))

        self.assertTrue(utils.validate_dni("1091272102"))
        self.assertTrue(utils.validate_dni("43381789"))
        self.assertFalse(utils.validate_dni("ABCDEF123456"))
        self.assertFalse(utils.validate_dni("123"))
        self.assertFalse(utils.validate_dni("1.091.272.102"))
        self.assertFalse(utils.validate_dni("1-091-272-102"))
        self.assertFalse(utils.validate_dni("1 091 272 102"))

        self.assertTrue(utils.validate_items("antibiotic_1", "10ml", "bovino", 12000))
        self.assertFalse(utils.validate_items("antibiotic_1", "", "bovino", 12000))


if __name__ == '__main__':
    unittest.main()
