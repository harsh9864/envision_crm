import frappe 

@frappe.whitelist()
def create_quotation(cost_estimation_id, opportunity):
    try:
        # Fetch Opportunity details (opportunity_from and party_name)
        opportunity_details = frappe.get_value(
            "Opportunity",
            opportunity,
            ["opportunity_from", "party_name", "custom_department","custom_project_type"],
            as_dict=True,
        )

        if not opportunity_details:
            frappe.throw(("Opportunity not found"))

        # Fetch and sort Quotation Selling Items by 'idx'
        sorted_quotation_selling_items = frappe.get_all(
            "Quotation Selling Items",
            filters={"parent": cost_estimation_id},
            fields=["item_code", "quantity", "rate", "amount", "idx"],
            order_by="idx",
        )

        if not sorted_quotation_selling_items:
            frappe.throw(
                ("No selling items found for cost estimation {0}").format(
                    cost_estimation_id
                )
            )

        # Create and populate Quotation
        new_quotation = frappe.new_doc("Quotation")
        new_quotation.update(
            {
                "quotation_to": opportunity_details.opportunity_from,
                "party_name": opportunity_details.party_name,
                "custom_department": opportunity_details.custom_department,
                "custom_project_type":opportunity_details.custom_project_type,
                "custom_cost_estimation": cost_estimation_id,
            }
        )

        # Append items in one loop
        for item in sorted_quotation_selling_items:
            new_quotation.append(
                "items",
                {
                    "item_code": item.item_code,
                    "qty": item.quantity,
                    "rate": item.rate,
                    "amount": item.amount,
                },
            )

        # Insert the new Quotation document into the database and commit
        new_quotation.insert(ignore_permissions=True)
        frappe.db.commit()
        frappe.msgprint("Quotation created successfully")

        return {"status": "success", "message":("Quotation created successfully")}

    except frappe.DoesNotExistError as e:
        frappe.log_error(f"Document not found: {str(e)}", "create_quotation")
        return {"status": "error", "message": f"Document not found: {str(e)}"}