class DataValidator:
    def validate(self, input_list):
        valid_numbers = []
        for item in input_list:
            if item.isdigit():
                valid_numbers.append(int(item)) #corrected again
        return valid_numbers
