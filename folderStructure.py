from folder_structure import FolderStructureGenerator
folders_to_ignore = [
    "__pycache__",
    ".git",
]

folder_structure_generator = FolderStructureGenerator(ignored_folders=folders_to_ignore)
folder_structure_md = folder_structure_generator.generate_folder_structure_md()
print(folder_structure_md)
