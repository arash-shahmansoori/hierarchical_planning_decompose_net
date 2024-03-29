import json
import re
from typing import NoReturn

from model import create_client
from prompts import sys_prompt_multi_layer_planning, usr_prompt_multi_layer_planning
from tqdm import tqdm


def create_dataset_rows(count: int = 0, N: int = 5) -> NoReturn:
    """Create rows of dataset.

    Args:
        count (int, optional): Count number. Defaults to 0.
        N (int, optional): Number of dataset files each with given rows. Defaults to 25.

    Returns:
        NoReturn:
    """

    client = create_client()

    for i in tqdm(range(N)):

        file_name = f"multi_layer_plan_multi_modal_task_decomp_{count+i}.json"

        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {
                    "role": "system",
                    "content": sys_prompt_multi_layer_planning,
                },
                {"role": "user", "content": usr_prompt_multi_layer_planning},
            ],
            temperature=1,
        )

        result = response.choices[0].message.content

        result_match = re.search("```json", result)

        # if result_match:
        #     result = json.loads(result.strip("```json"))
        # else:
        #     result = json.loads(result)

        try:
            result = json.loads(result)

            with open(f"data_multi_layer_planning/{file_name}", "w") as file:
                json.dump(result, file, indent=4)

        except json.decoder.JSONDecodeError:
            print("Failed to decode:")
            continue  # Continue to the next item in the loop
