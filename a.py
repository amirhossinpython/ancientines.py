from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.core.clipboard import Clipboard
from kivy.uix.popup import Popup
from kivy.uix.slider import Slider
from kivy.graphics import Color, Rectangle

english_to_pahlavi_mapping = {
    'A': '𐎠', 'B': '𐎡', 'C': '𐎤', 'D': '𐎣', 'E': '𐎠',
    'F': '𐎦', 'G': '𐎥', 'H': '𐎢', 'I': '𐎡', 'J': '𐎤',
    'K': '𐎣', 'L': '𐎲', 'M': '𐎫', 'N': '𐎱', 'O': '𐎺',
    'P': '𐎡', 'Q': '𐎥', 'R': '𐎼', 'S': '𐎴', 'T': '𐎮',
    'U': '𐎺', 'V': '𐎺', 'W': '𐎺', 'X': '𐎤', 'Y': '𐎡',
    'Z': '𐎳',
    'a': '𐎠', 'b': '𐎡', 'c': '𐎤', 'd': '𐎣', 'e': '𐎠',
    'f': '𐎦', 'g': '𐎥', 'h': '𐎢', 'i': '𐎡', 'j': '𐎤',
    'k': '𐎣', 'l': '𐎲', 'm': '𐎫', 'n': '𐎱', 'o': '𐎺',
    'p': '𐎡', 'q': '𐎥', 'r': '𐎼', 's': '𐎴', 't': '𐎮',
    'u': '𐎺', 'v': '𐎺', 'w': '𐎺', 'x': '𐎤', 'y': '𐎡',
    'z': '𐎳'
}


english_to_manichaean_mapping = {
    'A': '𐫀', 'B': '𐫁', 'C': '𐫄', 'D': '𐫆', 'E': '𐫀',
    'F': '𐫌', 'G': '𐫍', 'H': '𐫅', 'I': '𐫓', 'J': '𐫄',
    'K': '𐫍', 'L': '𐫎', 'M': '𐫏', 'N': '𐫐', 'O': '𐫑',
    'P': '𐫡', 'Q': '𐫍', 'R': '𐫇', 'S': '𐫈', 'T': '𐫃',
    'U': '𐫑', 'V': '𐫑', 'W': '𐫑', 'X': '𐫄', 'Y': '𐫓',
    'Z': '𐫧',
    'a': '𐫀', 'b': '𐫁', 'c': '𐫄', 'd': '𐫆', 'e': '𐫀',
    'f': '𐫌', 'g': '𐫍', 'h': '𐫅', 'i': '𐫓', 'j': '𐫄',
    'k': '𐫍', 'l': '𐫎', 'm': '𐫏', 'n': '𐫐', 'o': '𐫑',
    'p': '𐫡', 'q': '𐫍', 'r': '𐫇', 's': '𐫈', 't': '𐫃',
    'u': '𐫑', 'v': '𐫑', 'w': '𐫑', 'x': '𐫄', 'y': '𐫓',
    'z': '𐫧'
}
english_to_manichaean_mapping.update(
    {
    '-': '𐎽', '/': '𐏁', '+': '𐏃', '÷': '𐏄', '!': '𐏂',
    '#': '𐏃', '%': '𐏀', '^': '𐎼', '$': '𐏅', '"': '𐎿',
    '>': '𐏆', '<': '𐏇', 'ء': '𐎠', 'أ': '𐎡', 'إ': '𐎢',
    'ؤ': '𐎣', 'ژ': '𐎤', 'ي': '𐎥', 'ة': '𐎦', 'ِ': '𐎧',
    'ّ': '𐎨', 'ۀ': '𐎩', 'آ': '𐎪', 'ـ': '𐎫', '؛': '𐎬',
    '،': '𐎭', 'ريال': '𐎮', ',': '𐎯', ']': '𐎰', '[': '𐎱',
    '\\': '𐎲', '»': '𐎳', '&': '𐎴', '*': '𐎵', '(': '𐎶',
    ')': '𐎷'
    # بقیه کاراکترهای خاص را می‌توان اضافه کرد
}
)

english_to_cuneiform_mapping = {
    'a': '𒀀', 'b': '𒁀', 'c': '𒄀', 'd': '𒁲', 'e': '𒂊',
    'f': '𒆳', 'g': '𒄖', 'h': '𒄩', 'i': '𒄿', 'j': '𒋛',
    'k': '𒆠', 'l': '𒇻', 'm': '𒈠', 'n': '𒉈', 'o': '𒌋',
    'p': '𒉿', 'q': '𒆥', 'r': '𒊑', 's': '𒊍', 't': '𒋗',
    'u': '𒌑', 'v': '𒅅', 'w': '𒉿', 'x': '𒍝', 'y': '𒅀',
    'z': '𒍣',
    'A': '𒀀', 'B': '𒁀', 'C': '𒄀', 'D': '𒁲', 'E': '𒂊',
    'F': '𒆳', 'G': '𒄖', 'H': '𒄩', 'I': '𒄿', 'J': '𒋛',
    'K': '𒆠', 'L': '𒇻', 'M': '𒈠', 'N': '𒉈', 'O': '𒌋',
    'P': '𒉿', 'Q': '𒆥', 'R': '𒊑', 'S': '𒊍', 'T': '𒋗',
    'U': '𒌑', 'V': '𒅅', 'W': '𒉿', 'X': '𒍝', 'Y': '𒅀',
    'Z': '𒍣'
}

persian_to_cuneiform_mapping = {
    'آ': '𒀀', 'ا': '𒀀', 'ب': '𒁀', 'پ': '𒁀', 'ت': '𒁲',
    'ث': '𒁲', 'ج': '𒄀', 'چ': '𒄀', 'ح': '𒄩', 'خ': '𒄩',
    'د': '𒁲', 'ذ': '𒁲', 'ر': '𒊑', 'ز': '𒍣', 'ژ': '𒍣',
    'س': '𒊍', 'ش': '𒊍', 'ص': '𒋗', 'ض': '𒋗', 'ط': '𒋗',
    'ظ': '𒋗', 'ع': '𒆳', 'غ': '𒆳', 'ف': '𒆥', 'ق': '𒆥',
    'ک': '𒆠', 'گ': '𒄖', 'ل': '𒇻', 'م': '𒈠', 'ن': '𒉈',
    'و': '𒌋', 'ه': '𒂊', 'ی': '𒅀'
}
persian_to_cuneiform_mapping.update(
    {
        'ئ''𐎠',
    }
)
persian_to_pahlavi_mapping = {
    'آ': '𐎠', 'ا': '𐎠', 'ب': '𐎡', 'پ': '𐎡', 'ت': '𐎮',
    'ث': '𐎮', 'ج': '𐎤', 'چ': '𐎤', 'ح': '𐎢', 'خ': '𐎢',
    'د': '𐎣', 'ذ': '𐎣', 'ر': '𐎼', 'ز': '𐎳', 'ژ': '𐎳',
    'س': '𐎴', 'ش': '𐎴', 'ص': '𐎧', 'ض': '𐎧', 'ط': '𐎧',
    'ظ': '𐎧', 'ع': '𐎦', 'غ': '𐎦', 'ف': '𐎦', 'ق': '𐎦',
    'ک': '𐎠', 'گ': '𐎵', 'ل': '𐎲', 'م': '𐎫', 'ن': '𐎱',
    'و': '𐎺', 'ه': '𐎺', 'ی': '𐎡'
}
persian_to_pahlavi_mapping.update(
    {
        'ئ''𐎠',
    }

)
persian_to_pahlavi_mapping.update(
       {
    '-': '𐎽', '/': '𐏁', '+': '𐏃', '÷': '𐏄', '!': '𐏂',
    '#': '𐏃', '%': '𐏀', '^': '𐎼', '$': '𐏅', '"': '𐎿',
    '>': '𐏆', '<': '𐏇', 'ء': '𐎠', 'أ': '𐎡', 'إ': '𐎢',
    'ؤ': '𐎣', 'ژ': '𐎤', 'ي': '𐎥', 'ة': '𐎦', 'ِ': '𐎧',
    'ّ': '𐎨', 'ۀ': '𐎩', 'آ': '𐎪', 'ـ': '𐎫', '؛': '𐎬',
    '،': '𐎭', 'ريال': '𐎮', ',': '𐎯', ']': '𐎰', '[': '𐎱',
    '\\': '𐎲', '»': '𐎳', '&': '𐎴', '*': '𐎵', '(': '𐎶',
    ')': '𐎷'
    # بقیه کاراکترهای خاص را می‌توان اضافه کرد
}
)
persian_to_manichaean_mapping = {
    'آ': '𐫀', 'ا': '𐫀', 'ب': '𐫁', 'پ': '𐫡', 'ت': '𐫃',
    'ث': '𐫣', 'ج': '𐫄', 'چ': '𐫤', 'ح': '𐫅', 'خ': '𐫥',
    'د': '𐫆', 'ذ': '𐫦', 'ر': '𐫇', 'ز': '𐫧', 'ژ': '𐫨',
    'س': '𐫈', 'ش': '𐫩', 'ص': '𐫉', 'ض': '𐫪', 'ط': '𐫊',
    'ظ': '𐫫', 'ع': '𐫋', 'غ': '𐫬', 'ف': '𐫌', 'ق': '𐫭',
    'ک': '𐫍', 'گ': '𐫮', 'ل': '𐫎', 'م': '𐫏', 'ن': '𐫐',
    'و': '𐫑', 'ه': '𐫒', 'ی': '𐫓'
}
persian_to_cuneiform_mapping.update(
    {
    '-': '𐎽', '/': '𐏁', '+': '𐏃', '÷': '𐏄', '!': '𐏂',
    '#': '𐏃', '%': '𐏀', '^': '𐎼', '$': '𐏅', '"': '𐎿',
    '>': '𐏆', '<': '𐏇', 'ء': '𐎠', 'أ': '𐎡', 'إ': '𐎢',
    'ؤ': '𐎣', 'ژ': '𐎤', 'ي': '𐎥', 'ة': '𐎦', 'ِ': '𐎧',
    'ّ': '𐎨', 'ۀ': '𐎩', 'آ': '𐎪', 'ـ': '𐎫', '؛': '𐎬',
    '،': '𐎭', 'ريال': '𐎮', ',': '𐎯', ']': '𐎰', '[': '𐎱',
    '\\': '𐎲', '»': '𐎳', '&': '𐎴', '*': '𐎵', '(': '𐎶',
    ')': '𐎷'
    # بقیه کاراکترهای خاص را می‌توان اضافه کرد
}
)
persian_to_manichaean_mapping.update(
    {'ئ':'𐎠'}
)

english_to_pahlavi_mapping.update({
    '0': '𐏎', '1': '𐏑', '2': '𐏒', '3': '𐏓', '4': '𐏔',
    '5': '𐏕', '6': '𐏖', '7': '𐏗', '8': '𐏘', '9': '𐏙'
})

english_to_manichaean_mapping.update({
    '0': '𐫰', '1': '𐫱', '2': '𐫲', '3': '𐫳', '4': '𐫴',
    '5': '𐫵', '6': '𐫶', '7': '𐫷', '8': '𐫸', '9': '𐫹'
})

english_to_cuneiform_mapping.update({
    '0': '𒐀', '1': '𒐁', '2': '𒐂', '3': '𒐃', '4': '𒐄',
    '5': '𒐅', '6': '𒐆', '7': '𒐇', '8': '𒐈', '9': '𒐉'
})


english_to_cuneiform_mapping.update(
    {
    '-': '𐎽', '/': '𐏁', '+': '𐏃', '÷': '𐏄', '!': '𐏂',
    '#': '𐏃', '%': '𐏀', '^': '𐎼', '$': '𐏅', '"': '𐎿',
    '>': '𐏆', '<': '𐏇', 'ء': '𐎠', 'أ': '𐎡', 'إ': '𐎢',
    'ؤ': '𐎣', 'ژ': '𐎤', 'ي': '𐎥', 'ة': '𐎦', 'ِ': '𐎧',
    'ّ': '𐎨', 'ۀ': '𐎩', 'آ': '𐎪', 'ـ': '𐎫', '؛': '𐎬',
    '،': '𐎭', 'ريال': '𐎮', ',': '𐎯', ']': '𐎰', '[': '𐎱',
    '\\': '𐎲', '»': '𐎳', '&': '𐎴', '*': '𐎵', '(': '𐎶',
    ')': '𐎷'
    # بقیه کاراکترهای خاص را می‌توان اضافه کرد
}
)


def convert_to_cuneiform(text):
    return ''.join(english_to_cuneiform_mapping.get(char, persian_to_cuneiform_mapping.get(char, char)) for char in text)

def convert_to_pahlavi(text):
    return ''.join(english_to_pahlavi_mapping.get(char, persian_to_pahlavi_mapping.get(char, char)) for char in text)

def convert_to_manichaean(text):
    return ''.join(english_to_manichaean_mapping.get(char, persian_to_manichaean_mapping.get(char, char)) for char in text)



class ConverterApp(App):
    def build(self):
        self.title = "Text Converter to Ancient Scripts"
        self.font_size = 20
        self.text_color = (0, 0, 0, 1)  # Default text color is black

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Background color
        with layout.canvas.before:
            Color(1, 1, 1, 1)  # White background
            self.rect = Rectangle(size=layout.size, pos=layout.pos)
            layout.bind(size=self._update_rect, pos=self._update_rect)

        self.input_text = TextInput(
            hint_text='Enter text here',
            multiline=True,
            font_size=self.font_size,
            size_hint=(1, 0.3),
            background_color=(1, 1, 1, 1),  # White background for text input
            foreground_color=(0, 0, 0, 1)  # Black text
        )

        self.result_label = Label(
            text="Converted text will appear here",
            font_size=self.font_size,
            color=self.text_color,
            size_hint=(1, 0.3),
            halign='left',
            valign='middle'
        )

        self.spinner = Spinner(
            text='Select script',
            values=('Cuneiform', 'Pahlavi', 'Manichaean'),
            size_hint=(1, 0.1)
        )
        self.spinner.bind(text=self.on_spinner_select)

        self.size_slider = Slider(
            min=12,
            max=48,
            value=self.font_size,
            step=2,
            size_hint=(1, 0.1),
            orientation='horizontal'
        )
        self.size_slider.bind(value=self.on_size_slide)

        convert_button = Button(
            text='Convert Text',
            background_color=(0, 0.5, 1, 1),  # Blue
            color=(1, 1, 1, 1),  # White text
            font_size=24,
            size_hint=(1, 0.1)
        )
        convert_button.bind(on_press=self.convert_text)

        copy_button = Button(
            text='Copy to Clipboard',
            background_color=(0, 0.8, 0.2, 1),  # Green
            color=(1, 1, 1, 1),  # White text
            font_size=24,
            size_hint=(1, 0.1)
        )
        copy_button.bind(on_press=self.copy_to_clipboard)

        reset_button = Button(
            text='Reset',
            background_color=(1, 0, 0, 1),  # Red
            color=(1, 1, 1, 1),  # White text
            font_size=24,
            size_hint=(1, 0.1)
        )
        reset_button.bind(on_press=self.reset_fields)

        layout.add_widget(self.input_text)
        layout.add_widget(self.spinner)
        layout.add_widget(self.size_slider)
        layout.add_widget(convert_button)
        layout.add_widget(copy_button)
        layout.add_widget(reset_button)
        layout.add_widget(self.result_label)

        return layout

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def on_spinner_select(self, spinner, text):
        self.selected_script = text

    def on_size_slide(self, slider, value):
        self.font_size = int(value)
        self.result_label.font_size = self.font_size
        self.input_text.font_size = self.font_size

    def convert_text(self, instance):
        input_text = self.input_text.text
        if self.selected_script == 'Cuneiform':
            converted_text = convert_to_cuneiform(input_text)
        elif self.selected_script == 'Pahlavi':
            converted_text = convert_to_pahlavi(input_text)
        elif self.selected_script == 'Manichaean':
            converted_text = convert_to_manichaean(input_text)
        else:
            converted_text = "Please select a script."

        self.result_label.text = converted_text
        self.result_label.color = self.text_color

    def copy_to_clipboard(self, instance):
        Clipboard.copy(self.result_label.text)
        popup = Popup(
            title='Success',
            content=Label(text='Text copied to clipboard!'),
            size_hint=(None, None),
            size=(200, 100)
        )
        popup.open()

    def reset_fields(self, instance):
        self.input_text.text = ''
        self.result_label.text = 'Converted text will appear here'
        self.spinner.text = 'Select script'
        self.size_slider.value = 20

if __name__ == '__main__':
    ConverterApp().run()
