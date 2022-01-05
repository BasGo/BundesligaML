# Use this file to test your prediction algorithms.

from teamproject import models
import pandas as pd
import numpy as np


#downloading the pd dataframe for the second test_dataset
epl_1617 = pd.read_csv("http://www.football-data.co.uk/mmz4281/1617/E0.csv")
epl_1617 = epl_1617[['HomeTeam','AwayTeam','FTHG','FTAG']]
epl_1617 = epl_1617.rename(columns={'HomeTeam' : 'homeName',
                                    'AwayTeam' : 'guestName',
                                    'FTHG': 'homeScore',
                                    'FTAG': 'guestScore'})


# It is important to test your algorithms against handcrafted data to reliably
# cover edge cases! So feel free to make up several test datasets in the same
# format as would be returned by your crawler:
test_dataset = pd.DataFrame([
{"date": "2018-08-24T18:30:00Z", "homeName": "A", "guestName": "B", "homeScore": 3, "guestScore": 1},
{"date": "2018-08-24T18:30:00Z", "homeName": "A", "guestName": "B", "homeScore": 1, "guestScore": 2},
{"date": "2018-08-24T18:30:00Z", "homeName": "B", "guestName": "A", "homeScore": 3, "guestScore": 1},
{"date": "2018-08-24T18:30:00Z", "homeName": "A", "guestName": "B", "homeScore": 1, "guestScore": 1},
{"date": "2018-08-24T18:30:00Z", "homeName": "C", "guestName": "B", "homeScore": 2, "guestScore": 1}])


def test_BaselineAlgo():
    model = models.BaselineAlgo(test_dataset)
    prediction = model.predict

    # 4 matches between A and B of which B wins two and one ends in a draw
    assert np.allclose([sum(prediction('A', 'B')), sum(prediction('B', 'A'))], [1,1])
    assert prediction('A', 'B') == [0.25,0.25,0.5]
    assert prediction('B', 'A') == [0.5,0.25,0.25]

    # 1 match between B,C which  C  wins
    assert np.allclose([sum(prediction('C', 'B')), sum(prediction('B', 'C'))], [1,1])
    assert prediction('B', 'C') == [0,0,1]
    assert prediction('C', 'B') == [1,0,0]

    # No matches between A,C therefore return avg. probability
    assert np.allclose([sum(prediction('A', 'C')), sum(prediction('C', 'A'))], [1,1])
    assert prediction('A', 'C') == prediction('C', 'A') == [0.6,0.2,0.2]

    # No matches between A,D herefore return avg. probability
    assert np.allclose([sum(prediction('A', 'D')), sum(prediction('D', 'A'))], [1,1])
    assert prediction('A', 'D') == prediction('D', 'A') == [0.6,0.2,0.2]



def test_PoissonRegression():
    model = models.PoissonRegression(test_dataset)
    model_epl = models.PoissonRegression(epl_1617)
    prediction = model.predict
    epl_prediction = model_epl.predict

    # ensure that probabilities add up to one
    assert np.allclose([sum(prediction('A', 'B')),
                        sum(prediction('B', 'A')),
                        sum(prediction('C', 'B')),
                        sum(prediction('B', 'C'))], [1,1,1,1], rtol= 0.001,atol=0.001)

    # this is an example where the values where calculated by the Algo itself
    # but it ensures that its predictions don't change
    assert np.allclose(prediction('A', 'B'),[0.4544796774246377,
                                         0.2347542824035351,
                                         0.3107637450957457])
    assert np.allclose(prediction('B', 'A'),[0.7848852815728518,
                                         0.13235763774294387,
                                         0.08257250545683958])


    # outputs avg for unknown teams?
    assert np.allclose(prediction('AB', 'A'),[0.5591019448260419,
                                          0.2155308462270707,
                                          0.22535883848685306])
    assert np.allclose(prediction('AB', 'Bab'),[0.5591019448260419,
                                          0.2155308462270707,
                                          0.22535883848685306])

    # this example comes from the tutorial for this algorithm
    assert np.allclose(epl_prediction('Chelsea', 'Sunderland'),
                                        [0.8885986612364134,
                                         0.084093492686495977,
                                         0.026961819942853051],
                                         rtol=0.01,
                                         atol=0.01)
