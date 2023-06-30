#!/usr/bin/env python
"""
Module: priorityqueue_tests.py
Author: Reza Mousavi 
Date: June 29, 2023

This module contains unit tests for the PrioQueue class in the priorityqueue module.
"""
import sys
import io
import unittest
from lib.priorityqueue import PrioQueue

class PrioQueueTestCase(unittest.TestCase):
    """Test case for the PrioQueue class."""

    def setUp(self):
        """Set up the test case by initializing a PrioQueue and adding tasks."""
        self.queue = PrioQueue()
        self.queue.enqueue("Buy coffee for John", 1)
        self.queue.enqueue("Write a letter to Sarah", 5)
        self.queue.enqueue("Go shopping with Emma", 0)
        self.queue.enqueue("Pay bills", 9)
        self.queue.enqueue("Pay rent", 9)
        self.queue.enqueue("Do workout", 10)
        self.queue.enqueue("Clean up your room", 4)
        self.queue.enqueue("Call Peter", 5)
        self.queue.enqueue("Walk the dog", 3)

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

    def test_dequeue(self):
        """
        Test the dequeue method to ensure it removes and returns the highest-priority task.

        This test verifies that the dequeue method correctly removes and returns 
        the highest-priority task from the priority queue.
        It checks that the returned task is the one with the highest priority 
        and that the task is no longer in the queue after dequeueing.
        """
        highest_priority_task = self.queue.dequeue()
        self.assertEqual(highest_priority_task["priority"], 10)
        self.assertNotIn(highest_priority_task, self.queue.queue)

    def test_set_prio_order(self):
        """
        Test the set_prio_order method to ensure tasks are sorted correctly.

        This test validates that the set_prio_order method correctly sorts the tasks in 
        the priority queue based on their priorities and reception time.
        It checks that after calling set_prio_order, the tasks in the queue 
        are arranged in the expected order.
        """
        self.queue.set_prio_order()
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

    def test_process_tasks(self):
        """
        Test the process_tasks method to ensure tasks are processed in the correct order.

        This test verifies that the process_tasks method processes the tasks in the 
        priority queue in the correct order. It captures the output of the process_tasks 
        method and compares it with the expected output to ensure they match.
        """
        expected_output = "Processing command: Do workout (Priority: 10)\n" \
                        "Processing command: Pay bills (Priority: 9)\n" \
                        "Processing command: Pay rent (Priority: 9)\n" \
                        "Processing command: Write a letter to Sarah (Priority: 5)\n" \
                        "Processing command: Call Peter (Priority: 5)\n" \
                        "Processing command: Clean up your room (Priority: 4)\n" \
                        "Processing command: Walk the dog (Priority: 3)\n" \
                        "Processing command: Buy coffee for John (Priority: 1)\n" \
                        "Processing command: Go shopping with Emma (Priority: 0)\n"

        # Redirect stdout to capture the output of the print statements
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Call the process_tasks method
        self.queue.process_tasks()

        # Restore stdout and get the captured output
        sys.stdout = sys.__stdout__
        actual_output = captured_output.getvalue()
        self.assertEqual(actual_output, expected_output)



if __name__ == "__main__":
    unittest.main()
