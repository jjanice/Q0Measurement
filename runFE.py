from __future__ import print_function, division
from container import Cryomodule
from subprocess import CalledProcessError
from sys import stdout, stderr
from time import sleep

#GRAD_PV = "SEL_ASET"
GRAD_PV = "ADES"


if __name__ == "__main__":
    # noinspection PyUnboundLocalVariable

    #cavity = (Cryomodule(int(raw_input("SLAC CM: ")),
    #                     int(raw_input("JLAB CM: ")))
    #          .cavities[int(raw_input("Cavity: "))])
    cavity = Cryomodule(16, 2).cavities[7]

    try:
        #if GRAD_PV == "SEL_ASET":
            #cavity.checkAndSetOnTime()
            #cavity.phaseCavity()
        # step size of 0.5 corresponds to roughly 0.2 MV/m
        cavity.walkToGradient(desiredGradient=15.3, step=0.5, loopTime=2.5,
                              getFieldEmissionData=False, pv=GRAD_PV)
        cavity.walkToGradient(desiredGradient=8, step=0.1, loopTime=45, 
                              getFieldEmissionData=True, pv=GRAD_PV)

        #cavity.powerDown()

        
    except(CalledProcessError, IndexError, OSError, ValueError,
           AssertionError) as e:
        stderr.write("\nProcedure failed with error:\n{E}\n\n".format(E=e))
        sleep(0.01)
        cavity.powerDown()
