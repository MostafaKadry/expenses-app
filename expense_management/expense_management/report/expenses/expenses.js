frappe.query_reports["Expenses by Category"] = {

    
    // onload: function(report) {
    //     report.page.add_action("Export", function() {
    //         frappe.call({
    //             method: "frappe.desk.query_report.export_to_csv",
    //             args: {
    //                 report_name: "Expenses by Category",
    //                 filters: report.filters
    //             },
    //             callback: function(r) {
    //                 if (r.message) {
    //                     var url = r.message;
    //                     window.location.href = url;  
    //                 }
    //             }
    //         });
    //     });
    // },

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
