# -*- coding: utf-8 -*-
"""
@brief      test log(time=60s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version
import ensae_teaching_cs


class TestNotebookRunnerExpose1(unittest.TestCase):

    def setUp(self):
        fLOG("add missing dependencies", OutputPrint=__name__ == "__main__")
        add_missing_development_version(
            ["pyensae", "pymyinstall", "pymmails", "jyquickhelper"], __file__)

    def test_notebook_runner_expose1(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        from ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a
        temp = get_temp_folder(__file__, "temp_notebookexpose1_")
        keepnote = ls_notebooks("expose")
        execute_notebooks(temp, keepnote,
                          lambda i, n: "velib" not in n and "paris_parcours" not in n and
                          "ml_table_mortalite" not in n and "huge" not in n,
                          fLOG=fLOG,
                          clean_function=clean_function_1a,
                          dump=ensae_teaching_cs)


if __name__ == "__main__":
    unittest.main()
