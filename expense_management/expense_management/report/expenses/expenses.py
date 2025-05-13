import frappe

def execute(filters=None):
    user = frappe.session.user
    
    
    conditions = {"owner": user}
    
   
    if filters:
        if filters.get("from_date"):
            conditions["expense_date"] = [">=", filters.get("from_date")]
        if filters.get("to_date"):
            conditions["expense_date"] = ["<=", filters.get("to_date")]
        if filters.get("expense_category"):
            conditions["expense_category"] = filters.get("expense_category")
    
    
    data = frappe.get_all(
        "Expense",
        filters=conditions,
        fields=["expense_category", "expense_title", "expense_date", "amount", "description"]
    )
    
    grouped_data = frappe.get_all(
            "Expense",
            filters=conditions,
            fields=["expense_category", "SUM(amount) AS total_amount"],
            group_by="expense_category"
        )


    msg = f"Total Expenses: {sum([d.total_amount for d in grouped_data])} EGP"
    

    chart = {
        "data": {
            "labels": [d.expense_category for d in grouped_data],
            "datasets": [
                {
                    "name": "Total Expenses",
                    "values": [d.total_amount for d in grouped_data],
                }
            ],
        },
        "type": "bar",  
        "colors": ["#ff6f61", "#6a5acd", "#20c997", "#fcbf49", "#17a2b8"]
    }
    
    
    columns = [
        {"label": "Expense Category", "fieldname": "expense_category", "fieldtype": "Data"},
        {"label": "Expense Title", "fieldname": "expense_title", "fieldtype": "Data"},
        {"label": "Expense Date", "fieldname": "expense_date", "fieldtype": "Date"},
        {"label": "Amount (EGP)", "fieldname": "amount", "fieldtype": "Currency", "options": "EGP"},
        {"label": "Description", "fieldname": "description", "fieldtype": "Small Text"}
    ]
    
    
    return columns, data, msg, chart
