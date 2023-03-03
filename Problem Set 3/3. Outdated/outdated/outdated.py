month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


while True:
    try:
        # Getting date input in MM/DD/YYYY format.
        date_input = input('Date MM/DD/YYYY: ').strip().title()

        # If input is in MM/DD/YYYY format.
        if '/' in date_input:

            # Separating month, day & year in respective variables.
            m, d, y = date_input.split('/')

            # Checking if year is 4 digit, day is <= 31 & month is <= 12.
            if len(y) == 4 and int(d) <= 31 and int(m) <= 12:

                # If day & month both are less than 10.
                if int(d) <= 9 and int(m) <= 9:
                    print(f'{y}-0{m}-0{d}')
                    break

                # If day is greater than 10 but month is not.
                elif int(d) <= 9 < int(m):
                    print(f'{y}-{m}-0{d}')
                    break

                # If month is greater than 10 but day is not.
                elif int(d) > 9 >= int(m):
                    print(f'{y}-0{m}-{d}')
                    break

                # if day & month are greater or equal to 10.
                else:
                    print(f'{y}-{m}-{d}')
                    break

            # Checking if year is not 4 digit, day is not <= 31 & month is not <= 12.
            else:
                continue

        # If input is in september 8, 1636 format.
        else:
            # Splitting input on empty space.
            a, d, y = date_input.split()

            # Correcting value of day by removing ',' from the end.
            d = d[:-1]

            # Checking if inputted month in list & year of length & range of day is proper.
            if a in month and len(y) == 4 and int(d) <= 31:
                m = month.index(a) + 1

                # If month & day are less than 10.
                if 1 <= int(d) <= 9 and 1 <= int(m) <= 9:
                    print(f'{y}-0{m}-0{d}')
                    break

                # If month is <= 10 but day is less than 10.
                elif int(d) <= 9 < int(m):
                    print(f'{y}-{m}-0{d}')
                    break

                # If day is <= 10 but month is less than 10.
                elif int(d) > 9 >= int(m):
                    print(f'{y}-0{m}-{d}')
                    break

                # If month & day are greater than or equal to 10.
                else:
                    print(f'{y}-{m}-{d}')
                    break
                
            # Checking if inputted month not in list & year of length & range of day is not proper.
            else:
                continue

    # If input is in incorrect format.
    except ValueError:
        continue
        