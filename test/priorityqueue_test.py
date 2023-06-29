#!/usr/bin/env python
"""
Module: priorityqueue_tests.py
Author: Reza Mousavi (reza.mousavii@gmail.com)
Date: June 29, 2023

This module contains unit tests for the PrioQueue class in the priorityqueue module.
"""

import unittest
from lib.priorityqueue import PrioQueue

class PrioQueueTestCase(unittest.TestCase):
    """Test case for the PrioQueue class."""

    def setUp(self):
        """Set up the test case by initializing a PrioQueue and adding tasks."""
        self.queue = PrioQueue()
        self.queue.add_new_task("Buy coffee for John", 1)
        self.queue.add_new_task("Write a letter to Sarah", 5)
        self.queue.add_new_task("Go shopping with Emma", 0)
        self.queue.add_new_task("Pay bills", 9)
        self.queue.add_new_task("Pay rent", 9)
        self.queue.add_new_task("Do workout", 10)
        self.queue.add_new_task("Clean up your room", 4)
        self.queue.add_new_task("Call Peter", 5)
        self.queue.add_new_task("Walk the dog", 3)

    def test_queue_order(self):
        """Test the order of tasks in the priority queue."""
        expected_order = [
            "Do workout",
            "Pay bills",
            "Pay rent",
            "Write a letter to Sarah",
            "Call Peter",
            "Clean up your room",
            "Walk the dog",
            "Buy coffee for John",
            "Go shopping with Emma"
        ]
        actual_order = [task["command"] for task in self.queue.queue]
        self.assertEqual(actual_order, expected_order)

    def test_empty_queue(self):
        """Test that an empty priority queue has a length of 0."""
        empty_queue = PrioQueue()
        self.assertEqual(len(empty_queue.queue), 0)

    def test_string_representation(self):
        """Test the string representation of the priority queue."""
        expected_output = "Order: 1 - Task: Do workout\n" \
                        "Order: 2 - Task: Pay bills\n" \
                        "Order: 3 - Task: Pay rent\n" \
                        "Order: 4 - Task: Write a letter to Sarah\n" \
                        "Order: 5 - Task: Call Peter\n" \
                        "Order: 6 - Task: Clean up your room\n" \
                        "Order: 7 - Task: Walk the dog\n" \
                        "Order: 8 - Task: Buy coffee for John\n" \
                        "Order: 9 - Task: Go shopping with Emma\n"

        actual_output = str(self.queue)
        self.assertEqual(actual_output, expected_output)

if __name__ == "__main__":
    unittest.main()
