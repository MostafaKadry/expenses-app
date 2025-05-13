// Copyright (c) 2025, Mostafa K. and contributors
// For license information, please see license.txt

frappe.ui.form.on("Expense", {
    refresh(frm) {
        frm.trigger("amount")
        frm.trigger("expense_date")
    },
    amount(frm) {
        if (frm.doc.amount <= 0) {
            frm.set_df_property('amount', 'description', '<span style="color:red">Amount must be positive</span>');
            frappe.validated = false;
        } else {
            frm.set_df_property('amount', 'description', '');
        }
    },
    expense_date(frm) {
        if (frm.doc.expense_date > frappe.datetime.get_today()) {
            frm.set_df_property("expense_date", 'description', '<span style="color:red">Date Can\'t be in future</span>')
            frappe.validated = false;
        } else {
            frm.set_df_property('expense_date', 'description', '');
        }
    },
    after_save: (frm) => {
        frappe.call({
            method: "frappe.client.get_value",
            args: {
                doctype: "User",
                filters: { name: frappe.session.user },
                fieldname: "total_expenses"
            },
            callback: (r) => {
                if (r.message){
                    let total = r.message.total_expenses;
                    frappe.msgprint(`You have logged a total expenses of ${total} so far.`);
                }
            }
        })
    },
});
