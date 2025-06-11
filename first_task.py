def total_salary(path):
    try:
        total = 0
        count = 0
    
    #Use context manager to handle file operations
        with open(path, 'r', encoding = 'utf-8') as file:
            for line_number, line in enumerate(file,1):
            #Skip empty lines
                line = line.strip()
                if not line:
                    continue

                try:
                    #Split the line by comma 
                    parts = line.split(',')

                    #Verify that there are two lines
                    if len(parts) != 2:
                        raise ValueError(f"Invalid format on line {line_number}: '{line}'. Expected format: 'Name,Salary'")
                
                    name, salary_str = parts

                    #Verify that name is not empty
                    if not name.strip():
                        raise ValueError(f"Empty name on line {line_number}")
                
                    #Transform salary to float and check it
                    try:
                        salary = float(salary_str.strip())
                        if salary < 0:
                            raise ValueError(f"Negative salary on line {line_number}: {salary}")
                    
                    except ValueError as e:
                        if "could not convert" in str(e):
                            raise ValueError(f"Invalid salary format on line {line_number}: '{salary_str.strip()}'")
                    
                        else:
                            raise

                    total +=salary
                    count +=1
            
                except ValueError as e:
                    print(f"Warning: Skipping line {line_number} due to error: {e}")
                    continue

            if count ==0:
                raise ValueError("No salary record found in the file")

            #Calculate average
            average = total/count

            return(total, average)
        
    except FileNotFoundError:
        raise FileNotFoundError("File is not available in that path")
    
    except Exception as e:
        raise Exception(f"Unexpected error while processing file{path}: {str(e)}")

#Test the function
total, average = total_salary("first_task_text")
print(f"Загальна сума заробітної плати: {total}, середня заробітна плата: {average}")



                                     