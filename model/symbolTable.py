class SymbolTable:
    def __init__(self):
        self.table = {}
        self.count = 0

    def add(self, key):
        new_id = self.get_position(key)
        if new_id is not None:
            return new_id
        new_id = self.count
        self.table[key] = new_id
        self.count = self.count + 1
        return self.count - 1

    def get(self, key):
        return self.table[key]

    def get_position(self, key):
        return list(self.table).index(key) if key in self.table else None

    def print_st(self):
        for i in self.table.keys():
            print(f"{i:<30}{self.table[i]:<40}")

    def print_st_to_file(self, file):
        f = open(file, "w")
        f.write("ST: ")
        f.write("\n")
        for i in self.table.keys():
            f.write("\n")
            f.write(f"{i:<30}{self.table[i]:<40}")
        f.close()

        # f.write(
        #     "{0} {1} {2} {3}".format(
        #         filename.ljust(max_filename),
        #         type.rjust(max_type),
        #         size.rjust(max_size),
        #         modified.rjust(max_modified)
        #     )
        # )

# def main():
#     st = SymbolTable()
#     st.add("abc","int")
#     st.add("abcde","int")
#     st.add("abcd","int")
#     st.add("abc","int")
#
#     st.print_st()
#
#
# if __name__ == '__main__':
#     main()
