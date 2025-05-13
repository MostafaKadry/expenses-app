# Copyright (c) 2025, Mostafa K. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import today

class Expense(Document):
	def validate(self):
		if self.expense_date > today():
			frappe.throw("Date cannot be in future.")

		if self.amount <=0:
			frappe.throw("Expense Amount must be Positive")


	def on_update(self):
		user = self.owner
		total_expenses = self.get_total_expenses(user)
		self.update_user_total_expenses(user, total_expenses)


	def get_total_expenses(self, user):
		expenses = frappe.get_all('Expense', filters={'owner': user}, fields=['amount'])
		total_expenses = sum(expense.amount for expense in expenses)
		
		return total_expenses
	
	def update_user_total_expenses(self, user, total_expenses):
		frappe.db.set_value('User', user, 'total_expenses', total_expenses)


