frappe.ui.form.on("Material Request", {
    after_workflow_action:function(frm){
        if (frm.doc.workflow_state!="Approved by D-head"){
        frappe.call({
            method:"qoala_procurement.qoala_procurement.doctype.material_request.material_request.update_start_time",
            args:{
                "name": frm.doc.name
            },
            callback:function(r){
                frm.refresh()
            }
        })
    }
    }
});
    