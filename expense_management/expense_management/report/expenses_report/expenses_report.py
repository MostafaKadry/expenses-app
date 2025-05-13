# Copyright (c) 2025, Mostafa K. and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import getdate

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    return [
        {"label": "Expense Date", "fieldname": "expense_date", "fieldtype": "Date", "width": 100},
        {"label": "Expense Title", "fieldname": "expense_title", "fieldtype": "Data", "width": 150},
        {"label": "Expense Category", "fieldname": "expense_category", "fieldtype": "Data", "width": 120},
        {"label": "Amount", "fieldname": "amount", "fieldtype": "Currency", "width": 100},
        {"label": "Description", "fieldname": "description", "fieldtype": "Small Text", "width": 200}
    ]

def get_data(filters):
    conditions = {}

    if filters.get("expense_category"):
        conditions["expense_category"] = filters.get("expense_category")

    if filters.get("from_date") and filters.get("to_date"):
        # improve it to check first that the data_from is before to_date
        conditions["expense_date"] = ["between", [getdate(filters["from_date"]), getdate(filters["to_date"])]]

    conditions["owner"] = frappe.session.user

    return frappe.get_all(
        "Expense",
        filters=conditions,
        fields=[
            "expense_date",
            "expense_title",
            "expense_category",
            "amount",
            "description"
        ],
        order_by="expense_date desc"
    )


