# # stock prediciton use Root Mean Squared Error (RMSE) 
# # and Mean Absolute Percentage Error % (MAPE)

# class predictions: 
#     test_ratio = 0.2
#     training_ratio = 1 - test_ratio

#     train_size = int(training_ratio * len(stockprices))
#     test_size = int(test_ratio * len(stockprices))

#     train = stockprices[:train_size][['Date','Close']]
#     test = stockprices[train_size:][['Date','Close']]

#     def extract_seqX_outcomeY(self, data, N, offset):
#         X, y = [], []
        
#         for i in range(offset, len(data)):
#             X.append(data[i-N:i])
#             y.append(data[i])

#     def calculate_rmse(y_true, y_pred):
#         rmse = np.sqrt(np.mean((y_true-y_pred)**2))

#     def calculate_mape(y_true, y_pred)
#         y_pred, y_true = np.array(y_pred), np.array(y_true)
#         mape = np.mean(np.abs((y_true-t_pred) / y_true))*100
#         return mape