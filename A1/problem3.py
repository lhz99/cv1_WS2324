import numpy as np
import matplotlib.pyplot as plt


################################################################
#            DO NOT EDIT THESE HELPER FUNCTIONS                #
################################################################

# Plot 2D points
def displaypoints2d(points):
    plt.figure()
    plt.plot(points[0,:],points[1,:], '.b')
    plt.xlabel('Screen X')
    plt.ylabel('Screen Y')


# Plot 3D points
def displaypoints3d(points):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(points[0,:], points[1,:], points[2,:], 'b')
    ax.set_xlabel("World X")
    ax.set_ylabel("World Y")
    ax.set_zlabel("World Z")

################################################################


def gettranslation(v):
    """ Returns translation matrix T in homogeneous coordinates 
    for translation by v.

    Args:
        v: 3d translation vector

    Returns:
        Translation matrix in homogeneous coordinates
    """
    #
    # You code here
    #


def getyrotation(d):
    """ Returns rotation matrix Ry in homogeneous coordinates for 
    a rotation of d degrees around the y axis.

    Args:
        d: degrees of the rotation

    Returns:
        Rotation matrix
    """
    #
    # You code here
    #


def getxrotation(d):
    """ Returns rotation matrix Rx in homogeneous coordinates for a 
    rotation of d degrees around the x axis.

    Args:
        d: degrees of the rotation

    Returns:
        Rotation matrix
    """
    #
    # You code here
    #
    

def getzrotation(d):
    """ Returns rotation matrix Rz in homogeneous coordinates for a 
    rotation of d degrees around the z axis.

    Args:
        d: degrees of the rotation

    Returns:
        Rotation matrix
    """
    #
    # You code here
    #


def getcentralprojection(principal, focal):
    """ Returns the (3 x 4) matrix L that projects homogeneous camera 
    coordinates on homogeneous image coordinates depending on the 
    principal point and focal length.

    Args:
        principal: the principal point, 2d vector
        focal: focal length

    Returns:
        Central projection matrix
    """
    #
    # You code here
    #
    

def getfullprojection(T, Rx, Ry, Rz, L):
    """ Returns full projection matrix P and full extrinsic 
    transformation matrix M.

    Args:
        T: translation matrix
        Rx: rotation matrix for rotation around the x-axis
        Ry: rotation matrix for rotation around the y-axis
        Rz: rotation matrix for rotation around the z-axis
        L: central projection matrix

    Returns:
        P: projection matrix
        M: matrix that summarizes extrinsic transformations
    """
    #
    # You code here
    #


def cart2hom(points):
    """ Transforms from cartesian to homogeneous coordinates.

    Args:
        points: a np array of points in cartesian coordinates

    Returns:
        A np array of points in homogeneous coordinates
    """
    #
    # You code here
    #


def hom2cart(points):
    """ Transforms from homogeneous to cartesian coordinates.

    Args:
        points: a np array of points in homogenous coordinates

    Returns:
        A np array of points in cartesian coordinates
    """
    #
    # You code here
    #


def loadpoints(path):
    """ Load 2d points from file

    Args:
        path: Path of the .npy file
    Returns:
        Data as numpy array
    """
    #
    # You code here
    #


def loadz(path):
    """ Load z-coordinates from file

    Args:
        path: Path of the .npy file
    Returns:
        Data as numpy array
    """
    #
    # You code here
    #


def invertprojection(L, P2d, z):
    """
    Invert just the projection L of cartesian image coordinates 
    P2d with z-coordinates z.

    Args:
        L: central projection matrix
        P2d: 2d image coordinates of the projected points
        z: z-components of the homogeneous image coordinates

    Returns:
        3d cartesian camera coordinates of the points
    """
    #
    # You code here
    #


def inverttransformation(M, P3d):
    """ Invert just the model transformation in homogeneous 
    coordinates for the 3D points P3d in cartesian coordinates.

    Args:
        M: matrix summarizing the extrinsic transformations
        P3d: 3d points in cartesian coordinates

    Returns:
        3d points after the extrinsic transformations have been reverted
    """
    #
    # You code here
    #


def projectpoints(P, X):
    """ Apply full projection matrix P to 3D points X in cartesian coordinates.

    Args:
        P: projection matrix
        X: 3d points in cartesian coordinates

    Returns:
        x: 2d points in cartesian coordinates
    """
    #
    # You code here
    #


def p3multiplechoice(): 
    '''
    Change the order of the transformations (translation and rotation).
    Check if they are commutative. Make a comment in your code.
    Return 0, 1 or 2:
    0: The transformations do not commute.
    1: Only rotations commute with each other.
    2: All transformations commute.
    '''

    return -1
