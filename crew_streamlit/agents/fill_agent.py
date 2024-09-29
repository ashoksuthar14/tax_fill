from tools.filler import FormFiller

class FillAgent:
    def __init__(self, extracted_data, user_data):
        self.extracted_data = extracted_data
        self.user_data = user_data
        self.form_filler = FormFiller(form_path="./data/uploads/ITR_form.pdf")

    def fill_form(self):
        # Combine extracted data and user data for form filling
        combined_data = {**self.extracted_data, **self.user_data}
        
        # Fill the form with the combined data
        filled_form_path = self.form_filler.fill_form_with_data(combined_data)
        return filled_form_path
