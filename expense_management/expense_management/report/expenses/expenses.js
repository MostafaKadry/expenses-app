frappe.query_reports["Expenses by Category"] = {

    
    // Refresh the report after applying filters
    refresh: function(report) {
        const filters = report.filters;
        
        // When the filters change, re-fetch the data and chart
        frappe.call({
            method: "frappe.desk.query_report.run",
            args: {
                report_name: "Expenses by Category",
                filters: filters
            },
            callback: function(r) {
                if (r.message) {
                    report.set_data(r.message);
                }
            }
        });
    },

    // Handle the data filtering and table refresh
    ondata: function(report) {
        const filters = report.filters;
        
        // Call to fetch the data with the filters applied
        frappe.call({
            method: "frappe.desk.query_report.run",
            args: {
                report_name: "Expenses by Category",
                filters: filters
            },
            callback: function(r) {
                if (r.message) {
                    report.set_data(r.message);
                    report.refresh();
                }
            }
        });
    }
};
