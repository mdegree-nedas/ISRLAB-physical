# rcp: TEMPLATE MODULE
# rcp: auto-generated noros foreign template file
# rcp: EDIT this file and insert your callbacks


class Template:
    def ultrasound_read_callback(self):
        print("ultrasound.read.callback")

    def motion_go_forward_callback(self, data):
        print("motion.go_forward.callback")
        print("implement this method")
        print(data)
