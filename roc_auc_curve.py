import matplotlib.pyplot as plt
from sklearn.metrics import auc
from sklearn.metrics import roc_curve


def plot_roc_auc(X_train, y_train, X_test, y_test, all_clf, clf_labels):
    colors = ['black', 'orange', 'blue', 'purple', 'green', 'red', 'cyan']
    linestyles = [':', '--', '-.', '--', '-', '-', '-']
    for clf, label, clr, ls \
        in zip(all_clf,
               clf_labels, colors, linestyles):
        # assuming the label of the positive class is 1
        y_pred = clf.fit(X_train,
                         y_train).predict_proba(X_test)[:, 1]
        fpr, tpr, thresholds = roc_curve(y_true=y_test,
                                         y_score=y_pred)
        roc_auc = auc(x=fpr, y=tpr)
        plt.plot(fpr, tpr,
                 color=clr,
                 linestyle=ls,
                 label='%s (auc = %0.2f)' % (label, roc_auc))

    plt.legend(loc='lower right')
    plt.plot([0, 1], [0, 1],
             linestyle='--',
             color='gray',
             linewidth=2)

    plt.xlim([-0.1, 1.1])
    plt.ylim([-0.1, 1.1])
    plt.grid()
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')

    # plt.tight_layout()
    # plt.savefig('./figures/roc.png', dpi=300)
    plt.show()
