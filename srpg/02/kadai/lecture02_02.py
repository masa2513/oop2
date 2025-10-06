import xml.etree.ElementTree as ET

def lecture02_02() -> None:
    # XMLのルート要素（book）を作成
    root = ET.Element("book")
    
    # articleセクションを作成
    article = ET.SubElement(root, "article", title="卒業論文")
    
    # articleの各chapterを追加
    ET.SubElement(article, "chapter", id="1", name="はじめに", pages="2")
    ET.SubElement(article, "chapter", id="2", name="基礎理論", pages="8")
    ET.SubElement(article, "chapter", id="3", name="実験方法", pages="6")
    ET.SubElement(article, "chapter", id="4", name="結果と考察", pages="2")
    ET.SubElement(article, "chapter", id="5", name="まとめ", pages="1")
    ET.SubElement(article, "chapter", id="6", name="参考文献", pages="2")
    
    # novelセクションを作成
    novel = ET.SubElement(root, "novel")
    
    # novelの各chapterを追加
    ET.SubElement(novel, "chapter", id="1", name="1日のはじまり", pages="2")
    ET.SubElement(novel, "chapter", id="2", name="朝食", pages="8")
    ET.SubElement(novel, "chapter", id="3", name="仕事", pages="6")
    ET.SubElement(novel, "chapter", id="4", name="帰宅後", pages="2")
    ET.SubElement(novel, "chapter", id="5", name="新しい朝", pages="1")
    
    # XMLツリーを作成
    tree = ET.ElementTree(root)
    
    # XMLファイルに書き出し（インデント付きで整形）
    ET.indent(tree, space="  ", level=0)
    tree.write("lecture02_02_data.xml", encoding="UTF-8", xml_declaration=True)
    
    print("lecture02_02_data.xmlファイルを作成しました")

if __name__ == '__main__':
    lecture02_02()