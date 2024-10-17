# prompt_manager.py

class PromptManager:
    def __init__(self, db_module):
        self.db = db_module

    def create_prompt(self, name, content, samples, tags, version):
        prompt_data = {
            'name': name,
            'content': content,
            'version': version
        }
        prompt_id = self.db.insert('prompts', prompt_data)
        # Insert samples, tags, and other metadata
        self._add_samples(prompt_id, samples)
        self._add_tags(prompt_id, tags)
        return prompt_id

    def get_prompt(self, prompt_id, version=None):
        query = "SELECT * FROM prompts WHERE id = %s"
        params = [prompt_id]
        if version:
            query += " AND version = %s"
            params.append(version)
        result = self.db.execute_query(query, params)
        return result[0] if result else None

    def _add_samples(self, prompt_id, samples):
        # Assume samples is a dictionary with 'input' and 'output'
        data = {
            'prompt_id': prompt_id,
            'input_sample': samples['input'],
            'output_sample': samples['output']
        }
        self.db.insert('prompt_samples', data)

    def _add_tags(self, prompt_id, tags):
        for tag in tags:
            data = {'prompt_id': prompt_id, 'tag': tag}
            self.db.insert('prompt_tags', data)

