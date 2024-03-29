# Imports

from .scp_themes import get_marker, get_color

"""
========================
Method Name: ScatterPlot
========================

This method plots a 2D scatter graph using the matplotlib axis handle.


Parameters
========== 

axis                -   A matplotlib axis handle.

sc                  -   A single cell object which contains the data and metadata of genes and cells.

x                   -   A string for the column name in celldata assay of single cell (sc) object that 
                        contains the x-axis values.

y                   -   A string for the column name in celldata assay of single cell (sc) object that 
                        contains the y-axis values.

color_by            -   A string for the column name in celldata assay of single cell (sc) object that 
                        contains the cell clusters. A different color will be applied for each 
                        cluster. Clusters can be represented by string or numeric value.

marker_style        -   A string representing matplotlib markers. Refer to matplotlib documentation for
                        marker options.

marker_size         -   Integer representing matplotlib marker size. Refer to the matplotlib documentation 
                        for marker sizes.

legend_title        -   String representing the legend category. 


Returns
=======

axis                -   The matplotlib axis handle.

"""

def ScatterPlot(    axis,
                    sc, 
                    x,
                    y,
                    color_by, 
                    marker_style,
                    marker_size,
                    marker_color,
                    legend_title
                    ):


    X = sc.getCellData(x)

    Y = sc.getCellData(y)
    

    # To Do: Check if color_by is valid

    if (type(color_by) == str):

        cell_labels = sc.getNumericCellLabels(color_by)

        cell_types = sc.getDistinctCellTypes(color_by)
        

        if (type(cell_types[0]) != str):

            cell_types = cell_types.astype(str)


        for i in range(1, len(cell_types) + 1):

            mask = (cell_labels == i)

            axis.scatter(   x = X[mask],
                            y = Y[mask],
                            c = get_color(i-1),
                            marker = marker_style,
                            s = marker_size,
                            label = legend_title + '-' + cell_types[i-1] 
                            )

    else:
        
        axis.scatter(   x = X,
                        y = Y,
                        c = marker_color,
                        marker = marker_style,
                        s = marker_size,
                        label = legend_title
                        )

        
    

    # Temporarily remove marker size argument 26/07/2021

    return axis




def Scatter2D(  axis,
                sc, 
                x,
                y,
                color_by, 
                marker_by, 
                marker_style,
                marker_size
                ):

    
    if (type(marker_by) == str):

        cell_labels = sc.getNumericCellLabels(marker_by)
        cell_types = sc.getDistinctCellTypes(marker_by)

        
        if (type(cell_types[0]) != str):
            cell_types = cell_types.astype(str)

        # If marker_by == color_by?

        if (marker_by == color_by):

            for i in range(1, len(cell_types) + 1):
                mask = (cell_labels == i)
                axis = ScatterPlot( axis = axis,
                                    sc = sc[mask.tolist()],
                                    x = x,
                                    y = y,
                                    color_by = None,
                                    marker_style = get_marker(i-1),
                                    marker_size = marker_size,
                                    marker_color = get_color(i-1),
                                    legend_title = cell_types[i-1]
                                    )

            axis.legend(title = marker_by)
        
        else:

            for i in range(1, len(cell_types) + 1):
                mask = (cell_labels == i)
                axis = ScatterPlot( axis = axis,
                                    sc = sc[mask.tolist()],
                                    x = x,
                                    y = y,
                                    color_by = color_by,
                                    marker_style = get_marker(i-1),
                                    marker_size = marker_size,
                                    marker_color = get_color(0),
                                    legend_title = cell_types[i-1]
                                    )

            if (type(color_by) == str):

                axis.legend(title = marker_by + '-' + color_by)

            else:
                 
                axis.legend(title = marker_by)

    else:

        axis = ScatterPlot(     axis = axis,
                                sc = sc,
                                x = x,
                                y = y,
                                color_by = color_by,
                                marker_style = marker_style,
                                marker_size = marker_size,
                                marker_color = get_color(0),
                                legend_title = 'cluster'
                                )


        if (type(color_by) == str):

            axis.legend(title = color_by)


    axis.set_ylabel(x)
    axis.set_xlabel(y)

    return axis