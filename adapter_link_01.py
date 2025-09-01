import numpy as np
import matplotlib.pyplot as plt

def draw_Links(p0x, p0y, p1x, p1y, p2x, p2y, p3x, p3y, link_width):
    # draw link p0 to p1
    plt.plot([p0x, p1x], [p0y, p1y],'k', linewidth=link_width)

    # draw link p1 to p2
    plt.plot([p1x, p2x], [p1y, p2y],'k', linewidth=link_width)

    # draw output link p2 to p3
    plt.plot([p2x, p3x], [p2y, p3y],'k', linewidth=link_width)


def main():
    # start by setting the link constants and other plotting stuff


    v_scale = 1.5
    v_width = 1

    link_width = 1.1
    guide_width = 0.4
    guide_alpha = 0.4

    axlim = 3
    axshift = 2

    s = 2
    L1 = 1.25 * s / 2
    L3 = L1
    L2 = np.sqrt((2 * L1 - s)**2 + s**2) 
    print("L1 and L3 are %f\n" % L1)
    print("L2 is %f\n" % L2)

    # theta 1 in radians
    th1 = np.radians(0)
    print("theta 1 is %f\n" % th1)

    p0x = 0
    p0y = 0
    p1x = L1 * np.sin(th1)
    p1y = - L1 * np.cos(th1)
    
    p3x = s
    p3y = -s
    
    Lc = np.sqrt((p3x - p1x)**2 + (p3y - p1y)**2)
    print("Lc is %f\n" % Lc)
    
    term1 = (Lc**2 + L3**2 - L2**2)/(2 * Lc * L3)
    print("term1 is %f\n" % term1)
    
    alpha = np.arccos(term1)
    print("alpha is %f\n" % alpha)
    
    # theta c in radians
    thc = np.arctan2((p1y - p3y), (p3x - p1x)) 
    print("theta c is %f\n" % thc)
    
    # theta 3 in radians
    th3 = alpha + thc - np.radians(90)
    print("theta 3 is %f radians\n" % th3)
    
    # theta 3 in degrees
    th3_deg = np.degrees(th3)
    print("theta 3 in degrees is %f\n" % th3_deg)
    
    p2x = p3x + L3 * np.sin(th3)
    p2y = p3y + L3 * np.cos(th3)
    
    # set up the plot and draw some guide lines
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1, aspect='equal')
    ax.set_xlim((-axlim + axshift, axlim + axshift))
    ax.set_ylim((-axlim, axlim))
    plt.plot([-axlim + axshift, axlim + axshift], [0, 0],'k', linewidth=guide_width, alpha=guide_alpha)
    plt.plot([0, 0], [-axlim, axlim],'k', linewidth=guide_width, alpha=guide_alpha)
    plt.plot([-axlim + axshift, axlim + axshift], [-s, -s],'k', linewidth=guide_width, alpha=guide_alpha)
    plt.plot([s, s], [-axlim, axlim],'k', linewidth=guide_width, alpha=guide_alpha)
    
    # start drawing linkages!
    draw_Links(p0x, p0y, p1x, p1y, p2x, p2y, p3x, p3y, link_width)



    # show the plot!
    plt.show()





# name guard
if __name__ == "__main__":
    main()