#!/usr/bin/env python3


# Author: Raymond Malicdem


import unittest
import codeloader


class ModuleLImportLoaderTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("class based setup for the entire test case")

    @classmethod
    def teadDownClass(cls):
        print("class based tear down cleanup for the entire test case")

    def setUp(self):
        print("setup for each test item")

    def tearDown(self):
        print("tear down cleanup for each test item")

    def test_return_standalone_module(self):
        mod = codeloader.load_module_magic_import("loadable")
        self.assertIsNotNone(mod, "module object return is None")

    def test_standalone_module_object_instance_with_loadable_class(self):
        import loadable
        mod = codeloader.load_module_magic_import("loadable")
        self.assertTrue(isinstance(mod, loadable.__class__), "module object is not a class module")

    def test_standalone_module_object_instance_with_type_lodable(self):
        import loadable
        mod = codeloader.load_module_magic_import("loadable")
        self.assertTrue(isinstance(mod, type(loadable)), "module object is not of type class module")

    def test_standalone_module_object_instance_class_with_loadable_class_as_subclass(self):
        import loadable
        mod = codeloader.load_module_magic_import("loadable")
        self.assertTrue(
            issubclass(mod.__class__, loadable.__class__), 
            "module class is not the same class or subclass of loadable class"
        )    

    def test_standalone_module_object_instance_type_with_loadable_class_as_subclass(self):
        import loadable
        mod = codeloader.load_module_magic_import("loadable")
        self.assertTrue(
            issubclass(type(mod), loadable.__class__), 
            "type(module) is not the type or subclass of loadable class"
        )

    def test_standalone_module_object_instance_type_with_str_class_type(self):
        mod = codeloader.load_module_magic_import("loadable")
        self.assertFalse(isinstance(mod, str), "mod is an instance of str class type")

    def test_return_package_module(self):
        mod = codeloader.load_module_magic_import("loadables.loadable")
        self.assertIsNotNone(
            mod,
            "module object return is None",
        )

    def test_standalone_module_equality_between_explicit_import_and_dynamic_import(self):
        import loadable
        mod = codeloader.load_module_magic_import("loadable")
        self.assertEquals(
            mod, 
            loadable, 
            "dynmically imported module is different from the explicitly imported module"
        )

    def test_standalone_module_equality_between_loadable_module_and_sys_module(self):
        import sys
        mod = codeloader.load_module_magic_import("loadable")
        self.assertNotEqual(
            mod, 
            sys, 
            "dynmically imported standalone loadable module is same as the explicit sys imported module"
        )

    def test_standalone_module_package_equality(self):
        mod = codeloader.load_module_magic_import("loadable")
        self.assertEqual(
            mod.__package__, 
            "", 
            "dynamically imported standalone module package is not equal with provide value"
        )

    def test_standalone_module_package_equality_with_loadables_package(self):
        mod = codeloader.load_module_magic_import("loadable")
        self.assertNotEqual(
            mod.__package__, 
            "loadables", 
            "dynamically imported standalone module package is not equal with the loadables package"
        )

    def test_package_object_equality_between_dynamically_imported_and_explicity_imported(self):
        import loadables
        mod = codeloader.load_module_magic_import("loadables.loadable")
        self.assertEqual(
            mod, 
            loadables, 
            "dynamically package object is differemt with the explicitly imported loadables"
        )

    def test_package_values_equality_between_dynamically_imported_and_explicity_imported(self):
        mod = codeloader.load_module_magic_import("loadables.loadable")
        self.assertEqual(
            mod.__package__, 
            "loadables", 
            "package value of dynamically imported module is differemt with 'loadables' value"
        )

    def test_packaged_module_object_equality_between_dynamically_imported_and_explicity_imported(self):
        import loadables
        mod = codeloader.load_module_magic_import("loadables.loadable", "loadable")
        self.assertEqual(
            mod, 
            loadables.loadable, 
            "dynamically imported packaged module object is differemt with the explicitly imported loadables.loadable"
        )

    def test_packaged_module_values_equality_between_dynamically_imported_and_explicity_imported(self):
        mod = codeloader.load_module_magic_import("loadables.loadable", "lodables")
        self.assertEqual(
            mod.__package__, 
            "loadables", 
            "package value of dynamically imported module is differemt with 'loadables' value"
        )

    def test_module_object_equality_between_packaged_and_standalone(self):
        import loadables
        mods = codeloader.load_module_magic_import("loadable")
        modp = codeloader.load_module_magic_import("loadables.loadable", "lodables")
        self.assertNotEqual(
            mods, 
            modp, 
            "standalone lodable module is equalwith lodables.lodables "
        )

    def test_none_existing_standalone_module_returns_none_value(self):
        mod = codeloader.load_module_magic_import("nonexisting")
        self.assertIsNone(
            mod,
            "module object return is not None",
        )

    def test_none_existing_packaged_module_returns_none_value(self):
        mod = codeloader.load_module_magic_import("loadables.noneexisting", "lodables")
        self.assertIsNone(
            mod,
            "module object return is not None",
        )


class ModuleFunctionExtractTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("class based setup for the entire test case")

    @classmethod
    def teadDownClass(cls):
        print("class based tear down cleanup for the entire test case")

    def setUp(self):
        print("setup for each test item")

    def tearDown(self):
        print("tear down cleanup for each test item")

    def test_retured_function_object_from_dynamically_imported_module_is_not_none(self):
        mod = codeloader.load_module_magic_import("loadable")
        loadable_func = codeloader.get_function(mod, "triangle")
        self.assertIsNotNone(loadable_func, "function object from loadable module is None")

    def test_retured_function_object_from_dynamically_imported_module_is_none_with_not_existing_function(self):
        mod = codeloader.load_module_magic_import("loadable")
        loadable_func = codeloader.get_function(mod, "not_existing_function")
        self.assertIsNone(
            loadable_func, 
            "function from loadable module does not exist therefore None"
        )

    def test_function_object_equality_between_dynamically_loaded_function_and_explicitly_imported_module_function(self):
        import loadable
        mod = codeloader.load_module_magic_import("loadable")
        loadable_func = codeloader.get_function(mod, "triangle")
        self.assertEqual(
            loadable_func, 
            loadable.triangle,
            "function object from dynamic module is not equal with explicitly loadable.triangle"
        )

    def test_function_object_equality_between_dynamically_loaded_from_packaged_module_function_and_explicitly_imported_module_function(self):
        import loadables
        mod = codeloader.load_module_magic_import("loadables.loadable", "loadables")
        loadable_func = codeloader.get_function(mod, "most_number_element")
        self.assertEqual(
            loadable_func, 
            loadables.loadable.most_number_element,
            "function object from dynamic module is not equal with explicitly imported loadables.lodable.most_number_element"
        )

    def test_function_type_equality_betwwen_dynamic_function_from_standalone_module(self):
        import loadable
        mod = codeloader.load_module_magic_import("loadable")
        loadable_func = codeloader.get_function(mod, "triangle")
        self.assertIsInstance(
            loadable_func, 
            type(loadable.triangle),
            "function object type from dynamic module of type function from explicitly imported loadable.triangle"
        )

    def test_function_type_equality_betwwen_dynamic_function_from_packaged_module(self):
        import loadables
        mod = codeloader.load_module_magic_import("loadables.loadable", "loadables")
        loadable_func = codeloader.get_function(mod, "most_number_element")
        self.assertIsInstance(
            loadable_func, 
            type(loadables.loadable.most_number_element),
            "function object type from dynamic module of type function from explicitly imported loadables.lodable.most_number_element"
        )


if __name__ == "__main__":
    unittest.main()