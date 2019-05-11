import re

class ModuleOutput:
  def __init__(self):
    self.output1 = ''
    self.output2 = ''

  def get_output1(self):
    with open('output1.txt', 'r') as output1:
      lines = output1.read()
      self.output1 = lines.strip()

  def get_output2(self):
    module2_output = []
    formatted_result = []
    with open('output2.txt', 'r') as output2:
      lines = output2.read()
      for line in lines.split('\n'):
        line_after_arrow = re.sub(r'[^a-zA-Z0-9]+', ' ', line)   
        line_after_positions = line_after_arrow.replace('positions ','')
        line_after_through = line_after_positions.replace(' through', '')
        # Split by first 3 spaces only
        word_array = line_after_through.split(" ", 2)
        # Convert string numbers into integers
        for i in range(len(word_array)):
          if (word_array[i].isdigit()):
            word_array[i] = int(word_array[i])
        formatted_result.append(word_array)   
    return formatted_result



