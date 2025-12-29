from elements.base_element import BaseElement


class FileInput(BaseElement):
    def set_file_input(self, file: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        locator.set_input_files(file)
