from Move import Move

move_1 = Move(linear_x=2.0, linear_y=0.0, linear_z=0.0, angular_x=0.0, angular_y=0.0, angular_z=3.0)
print("Example filled object: ")
print(move_1, end="\n\n")

move_2 = Move()
print("Example empty object: ")
print(move_2, end="\n\n")

move_2.load_from_str(move_1.__str__())
print("Example empty object filled by filled object (json string): ")
print(move_2)
