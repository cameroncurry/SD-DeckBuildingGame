
def userStringInput(prompt, validInputs, complaint="Please Enter Valid Input:", retries=4):
    while True:
        x = raw_input(str(prompt)+"\n")
        if x in validInputs:
            return x
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint,', '.join('{}'.format(i) for i in validInputs)
