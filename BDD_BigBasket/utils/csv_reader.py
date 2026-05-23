import csv


class CSVReader:

    @staticmethod
    def read_csv(file_name):

        data = []

        with open(
                f"data/{file_name}",
                newline=""
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                data.append(row)

        return