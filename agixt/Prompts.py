import os


class Prompts:
    def add_prompt(self, prompt_name, prompt):
        # if prompts folder does not exist, create it
        if not os.path.exists("prompts"):
            os.mkdir("prompts")
        # if prompt file does not exist, create it
        if not os.path.exists(os.path.join("prompts", f"{prompt_name}.txt")):
            with open(os.path.join("prompts", f"{prompt_name}.txt"), "w") as f:
                f.write(prompt)

    def get_prompt(self, prompt_name, model="default"):
        model_prompt_file = f"prompts/{model}/{prompt_name}.txt"
        default_prompt_file = os.path.join("prompts", f"{prompt_name}.txt")

        prompt_file = (
            model_prompt_file
            if os.path.isfile(model_prompt_file)
            else default_prompt_file
        )
        with open(prompt_file, "r") as f:
            return f.read()

    def get_prompts(self):
        return [
            file.replace(".txt", "")
            for file in os.listdir("prompts")
            if file.endswith(".txt")
        ]

    def get_prompt_args(self, prompt_name):
        prompt = self.get_prompt(prompt_name)
        return [
            word[1:-1]
            for word in prompt.split()
            if word.startswith("{") and word.endswith("}")
        ]

    def delete_prompt(self, prompt_name):
        os.remove(os.path.join("prompts", f"{prompt_name}.txt"))

    def update_prompt(self, prompt_name, prompt):
        with open(os.path.join("prompts", f"{prompt_name}.txt"), "w") as f:
            f.write(prompt)

    def get_model_prompt(self, prompt_name, model="default"):
        with open(f"prompts/{model}/{prompt_name}.txt", "r") as f:
            return f.read()
