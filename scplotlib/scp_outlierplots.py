import numpy as np

from .scp_themes import get_color

"""
==============================
Method Name: PlotOutlierScores
==============================

Method Description: This method implements the proposed FeatClust approach. 


Parameters
========== 

axis                -   A matplotlib axis handle
sc                  -   A single cell object which contains the data and metadata of genes and cells



Returns
=======

axis                -   The matplotlib axis handle

"""

def PlotOutlierScores(
    axis,
    sc,
    outlier_score,
    color_by,
    threshold
):

    out_score = sc.getCellData(outlier_score)

    thres = sc.getCellData(threshold)


    cell_labels = sc.getNumericCellLabels(color_by)

    cell_types = sc.getDistinctCellTypes(color_by)


    idx = np.argsort(cell_labels)
    
    cell_labels = cell_labels[idx]

    out_score = out_score[idx]


    if (type(cell_types[0]) != str):

        for i in range(len(cell_types)):

            cell_types[i] = str(cell_types[i])


    x = np.arange(1, out_score.shape[0] + 1)


    for i in range(1, len(cell_types) + 1):

        mask = (cell_labels == i)

        axis.bar(x[mask], out_score[mask], color = get_color(i-1), label = cell_types[i-1])

    
    axis.legend(title = 'cell types', bbox_to_anchor=(1.2, 1))


    axis.plot(x, thres, color = 'black', linestyle = 'dashed')
    

    axis.set_ylabel(outlier_score)

    axis.set_xlabel('cells')

    
    return axis



