from inputs import ModuleOutput
from mappings import TAGS_MAPPING

class SocialNewsReader:
  def __init__(self):
    self.news_feed = ''
    self.module1 = ''
    self.module2 = []

  def get_modules(self):
    module_output = ModuleOutput()
    module_output.get_output1()
    module2_output = module_output.get_output2()
    self.module1 = module_output.output1
    self.module2 = sorted(module2_output, key = lambda start: start[0])

  def get_news_feed(self, module, start, end, tag_type, lowercase_tag):
    if tag_type is not None:
        if tag_type == 'a href':
          if lowercase_tag == 'twitter username':
            self.news_feed += module[start: start+1]
            start = start + 1
            self.news_feed += '<' + tag_type + '="http://twitter.com/' + module[start: end] + '">' + module[start: end] + '</a>'
          else:  
            self.news_feed += '<' + tag_type + '="' + module[start: end] + '">' + module[start: end] + '</a>'
        else:  
          self.news_feed += '<' + tag_type + '>' + module[start: end] + '</' + tag_type + '>'  
    else:
      self.news_feed += ' ' + module[start:end]    

  def build_modules(self):
    self.get_modules()
    s = self.module1
    indices = self.module2
    i = 0
    second = 1
    start = indices[i][0]
    end = indices[i][second]
    tag = indices[i][2]
    lowercase_tag = tag.lower().strip()
    if lowercase_tag in TAGS_MAPPING:
      tag_type = TAGS_MAPPING[lowercase_tag]

    while i < len(self.module2):
      self.get_news_feed(s, start, end, tag_type, lowercase_tag)
      if second == 0:
        start = end
        tag = indices[i][2]
        lowercase_tag = tag.lower().strip()
        if lowercase_tag in TAGS_MAPPING:
          tag_type = TAGS_MAPPING[lowercase_tag]
      else:
        start = end+1
        tag_type = None
      second = (second+1) % 2
      if second == 0:
        i += 1
      if i >= len(self.module2):
        break
      end = indices[i][second]
    return self.news_feed


if __name__ == '__main__':
  social_news_reader = SocialNewsReader()
  print social_news_reader.build_modules()
