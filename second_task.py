#The code reads a text file containing cat information and returns a list of dictionaries

def get_cats_info(path):
    try:
        cats_list = []

        #Open context manager to hanlde file operations
        with open(path, 'r', encoding = 'utf-8') as file:
            for line_number, line in enumerate(file,1):
                
                #Skip empty lines
                line = line.strip()
                if not line:
                    continue

                try:
                    #Split the line by comma
                    parts = line.split(',')

                    #Check that 3 parts were extracted (id, name, age)
                    if len(parts) != 3:
                        raise ValueError(f"Invalid format on line {line_number}: '{line}'. Expected format: 'id, name, age'")
                    
                    cat_id, name, age = parts

                    #Validate that all fiels have values
                    if not cat_id.strip():
                        raise ValueError(f'Empty cat ID on line {line_number}')
                    if not name.strip():
                        raise ValueError(f"Empty cat name on line {line_number}")
                    if not age.strip():
                        raise ValueError(f"Empty cat age on line {line_number}")
                    
                    #Validate age is a valide number
                    try:
                        age_int = int(age.strip())
                        if age_int < 0:
                            raise ValueError(f"Negative age on line {line_number}: {age_int}")
                    except ValueError as e:
                        if "invalid literal" in str(e):
                            raise ValueError(f"Invalid age format on line {line_number}: '{age.strip()}'. Age must be a number.")
                        else:
                            raise

                        #Create ditionary for the cat
                    cat_info = {
                        "id": cat_id.strip(),
                        "name": name.strip(),
                        "age": age.strip()
                    }

                    cats_list.append(cat_info)

                except ValueError as e:
                    print(f"Warning: Skipping line {line_number} due to error: {e}")
                    continue

        return cats_list
            
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")
    except PermissionError:
        raise PermissionError(f"File enconding error. Please ensure the file is UTF-8 encoded: {path}")
    except Exception as e:
        raise Exception(f"Unexpected error while processing file {path}: {str(e)}")

cats_info = get_cats_info("second_task_text")
print(cats_info)
