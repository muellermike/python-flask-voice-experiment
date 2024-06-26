from datalayers.exercise_datalayer import load_next_random_exercise, load_random_exercises
from datalayers.experiment_datalayer import load_user_experiment
from models.user import User

def get_exercises(answer: str, number_of_exercises: int):
    """
    gets a random ordered list of exercises which all have the correct answer provided as parameter
    """
    
    # loading all the possible exercises
    all_exercises = load_random_exercises(answer, number_of_exercises)
    
    return all_exercises

def get_next_random_exercise(experimend_id: int, user_id: int):
    """
    gets the next randomly selected exercise for the user experiment
    """

    # load the next exercise
    exercise = load_next_random_exercise(experimend_id, user_id)

    # when the exercise is None than there are two possibilities: either there is no experiment with this id for the user or there are no more exercises
    if exercise is None:
        # check whether the experiment for this user exists
        user_ex = load_user_experiment(experimend_id, user_id)
        if user_ex is None:
            # if the experiment for the user doesn't exist, return None
            return None
        else:
            # otherwise the experiment exists but there are no more exericeses to solve -> return empty object
            return ()

    return exercise