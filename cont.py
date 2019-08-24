# to set up an ISR use the time limit to read IMU values. I.e when we receive a value of theta at a time interval of 1000ms it will e updated
# into the controller function loop.
theta = "call the function"
theta_biased = "call the function"
torque = 0# intially considered zero
state_0 = 0
state_1 = 0

while(true):
    A = [[0,0],[0,0]]
    B = [[0,0,0],[0,0,0]]
    C = [0,0]
    D = #update the K value form the Matla

    def cont_s():
        ip_0 = 0 - theta
        ip_1 = 0 - theta_biased
        ip_2 = 0 - torque
        # in the above mentioned line we are r-z is calculated.
        # based on Ms Jackson's Pseudo code following controller code is written
        cont_out = c[0]*state_0 + c[1]*state_1 + D[0]*ip_0 + D[1]*ip_1 + D[2]*ip_2
        state_0 = A[0][0]*state_0 + A[0][1]*state_1 + B[0][0]*ip_0 + B[0][1]*ip_1 + B[0][2]*ip_2
        state_1 = A[1][0]*state_0 + A[1][1]*state_1 + B[1][0]*ip_0 + B[1][1]*ip_1 + B[1][2]*ip_2

        return cont_out

    torque = cont_s()

''' motor control code '''

#this is code hasn't been verified with any of the hardware. Try to run the kalaman and this together. Cont_s function will give you the torque
#output
