import unittest
from unittest.mock import patch
from ..main import main  # Import the main function from the app
from ..modules import cpu_details, disk_details, memory_details  # Import from modules

class TestSystemMonitor(unittest.TestCase):

    @patch('app.modules.cpu_details.run')  # Update import paths
    @patch('builtins.input', side_effect=['1', '0'])
    def test_cpu_details(self, mock_input, mock_cpu_run):
        with self.assertRaises(SystemExit):
            main()
        mock_cpu_run.assert_called_once()

    @patch('app.modules.disk_details.run')  # Update import paths
    @patch('builtins.input', side_effect=['2', '0'])
    def test_disk_details(self, mock_input, mock_disk_run):
        with self.assertRaises(SystemExit):
            main()
        mock_disk_run.assert_called_once()

    @patch('app.modules.memory_details.run')  # Update import paths
    @patch('builtins.input', side_effect=['3', '0'])
    def test_memory_details(self, mock_input, mock_memory_run):
        with self.assertRaises(SystemExit):
            main()
        mock_memory_run.assert_called_once()

    @patch('builtins.input', side_effect=['0'])
    def test_exit(self, mock_input):
        with self.assertRaises(SystemExit):
            main()

if __name__ == "__main__":
    unittest.main()
