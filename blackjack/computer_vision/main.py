from blackjack.computer_vision.model import load_roboflow_model, predict_roboflow_model
from blackjack.computer_vision.clustering import (
    cluster_one_player,
    cluster_one_player_advanced,
)


if __name__ == "__main__":
    try:
        model = load_roboflow_model()
        card_predictions_df = predict_roboflow_model(
            model=model, image_file_name="test_image.png"
        )
        result = cluster_one_player_advanced(card_predictions_df=card_predictions_df)
        print(result)
    except:
        import ipdb, traceback, sys

        extype, value, tb = sys.exc_info()
        traceback.print_exc()
        ipdb.post_mortem(tb)