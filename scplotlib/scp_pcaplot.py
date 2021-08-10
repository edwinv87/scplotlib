from sklearn.decomposition import PCA
from .scp_core import Scatter2D


"""
=======================
Method Name: ComputePCA
=======================

Computes and saves the first two principal components of the data in the 
celldata assay of the single cell object.


Parameters
========== 

sc                  -   A single cell object which contains the data and metadata of genes and cells

Returns
=======

sc                  -   The single cell object with the first two principal components of the 
                        data saved in the celldata assay.

"""

def ComputePCA(sc):

    X = sc.getCounts()
    pca = PCA(n_components=2)
    X_red = pca.fit_transform(X.T)
    x = X_red[:, 0]
    y = X_red[:, 1]

    sc.addCellData(col_data = x, col_name = 'PC1')
    sc.addCellData(col_data = y, col_name = 'PC2')

    return sc


"""
====================
Method Name: PCAPlot
====================

This method plots a 2D scatter graph using the matplotlib axis handle where x values
represent the first principal component and y values represent the second principal component in the
data. 


Parameters
========== 

axis                -   A matplotlib axis handle.

sc                  -   A single cell object which contains the data and metadata of genes and cells.

color_by            -   A string for the column name in celldata assay of single cell (sc) object that 
                        contains the cell clusters. A different color will be applied for each cluster. 
                        Clusters can be represented by string or numeric value. Default None.

marker_by           -   A string for the column name in celldata assay of single cell (sc) object that 
                        contains the cell clusters. A different marker style will be applied for each 
                        cluster. Clusters can be represented by string or numeric value. Default None.

marker_style        -   A string representing matplotlib markers. Refer to matplotlib documentation for
                        marker options. Default '.'.

marker_size         -   Integer representing matplotlib marker size. Refer to the matplotlib documentation 
                        for marker sizes. Default 50.


Returns
=======

axis                -   The matplotlib axis handle.

"""

def PCAPlot(    axis,
                sc, 
                color_by = None, 
                marker_by = None, 
                marker_style = '.',
                marker_size = 50
                ):

    sc = ComputePCA(sc)
    
    axis = Scatter2D(   axis = axis,
                        sc = sc, 
                        x = 'PC1',
                        y = 'PC2',
                        color_by = color_by, 
                        marker_by = marker_by, 
                        marker_style = marker_style,
                        marker_size = marker_size
                        )

    return axis