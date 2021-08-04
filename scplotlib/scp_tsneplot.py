from sklearn.manifold import TSNE
from .scp_core import ScatterPlot


from .scp_themes import get_marker

def ComputeTSNE(    sc, 
                    tsne_dist_metric,
                    tsne_init,
                    tsne_perplexity,
                    tsne_iterations,
                    tsne_learning_rate,
                    tsne_early_exaggeration,
                    tsne_random_state):

    tsne = TSNE(    n_components = 2, 
                    metric=tsne_dist_metric,
                    init= tsne_init,
                    perplexity=tsne_perplexity,
                    n_iter=tsne_iterations,
                    learning_rate=tsne_learning_rate,
                    early_exaggeration=tsne_early_exaggeration,
                    random_state=tsne_random_state
                    )

    X = sc.getCounts() # X is (features, samples)

    X_red = tsne.fit_transform(X.T)
    x = X_red[:, 0]
    y = X_red[:, 1]

    sc.addCellData(col_data = x, col_name = 't-SNE 1')
    sc.addCellData(col_data = y, col_name = 't-SNE 2')

    return sc



# Produces a t-SNE scatter plot
def tSNEPlot(   axis,
                sc, 
                color_by = None, 
                marker_by = None, 
                marker_style = '.',
                marker_size = 50,
                tsne_dist_metric = 'euclidean',
                tsne_init = 'random',
                tsne_perplexity = 30,
                tsne_iterations = 1000,
                tsne_learning_rate = 200,
                tsne_early_exaggeration = 12,
                tsne_random_state = None
                ):


    sc = ComputeTSNE(   sc, 
                        tsne_dist_metric,
                        tsne_init,
                        tsne_perplexity,
                        tsne_iterations,
                        tsne_learning_rate,
                        tsne_early_exaggeration,
                        tsne_random_state)

    if (type(marker_by) == str):
        cell_labels = sc.getNumericCellLabels(marker_by)
        cell_types = sc.getDistinctCellTypes(marker_by)

        
        if (type(cell_types[0]) != str):
            for i in range(len(cell_types)):
                cell_types[i] = str(cell_types[i])

        for i in range(1, len(cell_types) + 1):
            mask = (cell_labels == i)
            axis = ScatterPlot( axis,
                                sc[mask.tolist()],
                                x = 't-SNE 1',
                                y = 't-SNE 2',
                                color_by = color_by,
                                marker_style = get_marker(i-1),
                                marker_size = marker_size,
                                legend_title = cell_types[i-1] + '-'
                                )

        axis.legend(title = 'batch-cell type')

    else:
        axis = ScatterPlot(     axis,
                                sc,
                                x = 't-SNE 1',
                                y = 't-SNE 2',
                                color_by = color_by,
                                marker_style = marker_style,
                                marker_size = marker_size,
                                legend_title = ""
                                )

        axis.legend(title = 'cell type')

    axis.set_ylabel('t-SNE 2')
    axis.set_xlabel('t-SNE 1')

    return axis