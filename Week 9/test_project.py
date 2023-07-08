from final_project.project import game, generate_author, scrapping


def test_game():
    assert game == game


def test_generate_author():
    assert generate_author({1:2}) == (1,2)
    assert generate_author({"William Shakespeare":"British"}) == ("William Shakespeare","British")
    assert generate_author({9:"KT"}) == (9,"KT")
    assert generate_author({"Hajime Isayama":"Japanese"}) == ("Hajime Isayama","Japanese")


def test_scrapping():
    assert scrapping() == {'William Shakespeare': 'British', 'Agatha Christie': 'British', 'Barbara Cartland': 'British',
    'Danielle Steel': 'American', 'Harold Robbins': 'American', 'Georges Simenon': 'Belgian', 'J. K. Rowling': 'British',
    'Enid Blyton': 'British', 'Sidney Sheldon': 'American', 'Eiichiro Oda': 'Japanese', 'Gilbert Patten': 'American',
    'Dr. Seuss': 'American', 'Akira Toriyama': 'Japanese', 'Leo Tolstoy': 'Russian', 'Corín Tellado': 'Spanish',
    'Dean Koontz': 'American', 'Jackie Collins': 'British', 'Horatio Alger': 'American', 'Nora Roberts': 'American',
    'R. L. Stine': 'American', 'Alexander Pushkin': 'Russian', 'Stephen King': 'American', 'Paulo Coelho': 'Brazilian',
    'Jirō Akagawa': 'Japanese', 'Jeffrey Archer': 'British', "Louis L'Amour": 'American', 'René Goscinny': 'French',
    'Erle Stanley Gardner': 'American', 'Edgar Wallace': 'British', 'Janet Dailey': 'Chinese', 'Robert Ludlum': 'American',
    'Osamu Tezuka': 'Japanese', 'James Patterson': 'American', 'Frédéric Dard': 'French', 'Stan and Jan Berenstain': 'American',
    'Roald Dahl': 'British', 'John Grisham': 'American', 'Zane Grey': 'American', 'Irving Wallace': 'American',
    'J. R. R. Tolkien': 'British', 'Masashi Kishimoto': 'Japanese', 'Gosho Aoyama': 'Japanese', 'Karl May': 'German',
    'Mickey Spillane': 'American', 'C. S. Lewis': 'British', 'Kyotaro Nishimura': 'Japanese', 'Mitsuru Adachi': 'Japanese',
    'Rumiko Takahashi': 'Japanese', 'Dan Brown': 'American', 'Alistair MacLean': 'Scottish', 'Ann M. Martin': 'American',
    'Ryōtarō Shiba': 'Japanese', 'Arthur Hailey': 'British/Canadian', 'Astrid Lindgren': 'Swedish', 'Koyoharu Gotouge': 'Japanese',
    'Anne Rice': 'American', 'Gérard de Villiers': 'French', 'Beatrix Potter': 'British', 'Michael Crichton': 'American',
    'Richard Scarry': 'American', 'Clive Cussler': 'American', 'Ken Follett': 'British', 'Debbie Macomber': 'American',
    'Naoki Urasawa': 'British', 'Carter Brown': 'Japanese', 'Eiji Yoshikawa': 'Japanese', 'Catherine Cookson': 'British',
    'Stephenie Meyer': 'American', 'Norman Bridwell': 'American', 'David Baldacci': 'American', 'Hirohiko Araki': 'Japanese',
    'Evan Hunter': 'American', 'Andrew Neiderman': 'American', 'Roger Hargreaves': 'British', 'Robin Cook': 'American',
    'Wilbur Smith': 'South African/British', 'Erskine Caldwell': 'American', 'Eleanor Hibbert': 'British', 'Lewis Carroll':
    'British', 'Denise Robins': 'British', 'Cao Xueqin': 'Chinese', 'Ian Fleming': 'British', 'Hermann Hesse': 'German-Swiss',
    'Rex Stout': 'American', 'Anne Golon': 'French', 'Frank G. Slaughter': 'American', 'Edgar Rice Burroughs': 'American',
    'John Creasey': 'British', 'James A. Michener': 'Japanese', 'Seiichi Morimura': 'Japanese', 'Mary Higgins Clark': 'American',
    'Penny Jordan': 'British', 'Patricia Cornwell': 'American', 'Hajime Isayama': 'Japanese', 'Terry Pratchett': 'English'}
