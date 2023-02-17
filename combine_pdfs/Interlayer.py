from re import S
from fpdf import FPDF
from os import path, makedirs, remove


class InterlayerFactory():

    width_A4 = 210
    height_A4 = 297

    def __init__(self, folder: str) -> None:
        self.parent_dir, self.folder_name = path.split(folder)
        self.interlayer_folder = path.join(
            self.parent_dir, "_temp-interlayers")
        self.blank_page = path.join(self.interlayer_folder, "blank_page.pdf")

    def create_interlayer(self, root: str, files: list) -> str:
        """creates a pdf interlayer for specific folder with files.
        Both the path to the folder and the files inside it are listed in the pdf.
        The interlayer is saved in a common folder for interlayers.

        Args:
            root (str): root of the folder
            files (list): list of pdf files inside the folder

        Returns:
            str: the name of the interlayer generated in the interlayer's folder
        """

        _path, title = path.split(root)

        print("Creating interlayer " + title, end="\t")

        il = FPDF(orientation="P", unit="mm", format="A4")
        il.set_author("Jaime Alba")
        il.set_creator("Polytech Nice Conseil")

        il.add_page()
        self._add_border_lines(il)

        il.set_font(family="Arial", size=12)
        il.set_text_color(0, 0, 0)

        self._add_title(il, title)
        self._add_path(il, _path)
        self._table_of_content(il, files)

        # add page so number of pages is even
        self._make_even(il)

        self._check_common_folder()
        filename = self._generate_name(title)

        il.output(filename)
        il.close()

        print("done")
        return filename

    def _add_border_lines(self, pdf: FPDF) -> None:
        spc = 5
        pdf.rect(spc, spc, self.width_A4 - 2*spc,
                 self.height_A4-2*spc)

    def _table_of_content(self, pdf: FPDF, files: list) -> None:
        txt = "\n".join(files)

        pdf.set_xy(self.width_A4//10, self.height_A4//4)
        pdf.set_font_size(12)

        pdf.multi_cell(w=200, h=8, txt=txt)

    def _add_title(self, pdf: FPDF, title: str, cap: bool = True) -> None:
        if cap:
            title = title.upper()

        pdf.set_font_size(30)
        pdf.set_text_color(0, 0, 0)

        pdf.set_xy(0, self.height_A4//6)
        pdf.cell(w=self.width_A4, h=self.height_A4//16, txt=title, align='C')

    def _add_path(self, pdf: FPDF, root: str) -> None:
        root = root.replace("\\", "\n")
        root = root[len(self.parent_dir):]

        pdf.set_font_size(10)
        pdf.set_text_color(80, 80, 80)

        pdf.set_xy(20, 10)
        pdf.multi_cell(w=self.width_A4, h=4, txt=root)

    def _generate_name(self, title: str, ext: str = ".pdf") -> str:
        filename = path.join(self.interlayer_folder, title+ext)
        i = 1
        while path.exists(filename):
            filename = path.join(self.interlayer_folder, f"{title}_{i}{ext}")
            i += 1

        return filename

    def _check_common_folder(self):
        if not path.exists(self.interlayer_folder):
            makedirs(self.interlayer_folder)
        if not path.exists(self.blank_page):
            self._create_blank_page()

    def _create_blank_page(self):
        il = FPDF(orientation="P", unit="mm", format="A4")
        il.set_author("Jaime Alba")
        il.set_creator("Polytech Nice Conseil")

        il.add_page()

        il.output(self.blank_page)
        il.close()

    def _make_even(self, pdf: FPDF):

        if pdf.page_no() % 2 == 1:
            pdf.add_page()

    def close(self):
        if os.path.exists(self.interlayer_folder):
            os.remove(self.interlayer_folder)
        else:
            print("Inter-layer folder removed")
        pass

