from utils import generate_embeddings, split_into_chunk
import tqdm
import pandas as pd

text = """
List of plugins that integrate with TerminalView
The following is a list of known plugins that integrate with TerminalView.

SendCode by randy3k (https://github.com/randy3k/SendCode)
ShellVE by bfelder (https://github.com/bfelder/ShellVE)
Common problems
List of common problems you may encounter when using this plugin.

A keybinding is not working even though it is listed in the keybindings section
This is most likely because you have the key bound to something else in your user keymap file. To make it work find the missing keybinding in the TerminalView keymap and copy it to your user keymap. For details see the keybindings section above.

The terminal is responsive but acts weird (prints weird sequences, cursor located in the wrong place, etc.)
Ensure you do not have a bash_profile file or similar that changes the value of the TERM environment variable. This is set to “linux” by the plugin and must stay that way. You can check it by calling env | grep TERM inside the terminal view in ST3. If the TERM value is correct feel free to open an issue for further investigation.

The terminal is sluggish and/or uses a lot of memory
You may have other plugins that conflict with TerminalView. TerminalView does a lot of modifications to the buffer which can conflict with plugins like e.g. GotoLastEditEnhanced. In this particular case a history of all modifications are saved causing unbound memory usage. Please test TerminalView in isolation to see if the issue persists.

Acknowledgments
The pyte terminal emulator (https://github.com/selectel/pyte) is an integral part of this plugin and deserves some credit for making this plugin possible.

During development the SublimePTY plugin (https://github.com/wuub/SublimePTY) was a good source of inspiration for some of the problems that occurred. You can probably find a few bits and pieces from it in this plugin.

For testing stubs and general test structure the Javatar plugin (https://github.com/spywhere/Javatar) was a good point of origin.

"""

chunks = split_into_chunk(text, chunk_size=20)
print(chunks)
embeddings = []
for chunk in tqdm.tqdm(chunks, desc="proccessing chunks") :
  embedding = generate_embeddings(chunk)
  embeddings.append(embedding)
# embeddings = generate_embeddings
print(f"chunk length = {len(chunks)}")
print(f"chun : \n", chunks)

print(f"embedding length = {len(embeddings)}")
print(f"embedding : \n {embeddings}")


data_frame = pd.read_csv("users_embedding.csv")
new_row = {'username': "niraj", "filename": "random.pdf", "page_count": 20, "total_tokens": 2345, "chunks": chunks, "embeddings": embeddings }
data_frame = pd.concat([data_frame.iloc[:1], pd.DataFrame([new_row]), data_frame.iloc[1:]]).reset_index(drop=True)
data_frame.to_csv("users_embedding.csv", index=False)
