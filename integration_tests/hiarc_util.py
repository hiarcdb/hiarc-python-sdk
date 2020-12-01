import uuid
import hiarc
from random import choice
from datetime import datetime
import dateutil.parser
import os


class hiarc_util:

    curr_file = 0
    curr_coll = 0
    curr_user = 0
    curr_group = 0
    curr_retention_policy = 0
    curr_legal_hold = 0
    curr_classification = 0

    AWS_EAST_STORAGE = "hiarc-aws-s3-east"
    AWS_WEST_STORAGE = "hiarc-aws-s3-west"
    AZURE_STORAGE_1 = "hiarc-azure-blob-1"
    AZURE_STORAGE_2 = "hiarc-azure-blob-2"
    GOOGLE_EAST_STORAGE = "hiarc-google-storage-east"
    GOOGLE_WEST_STORAGE = "hiarc-google-storage-west"
    All_STORAGE_SERVICES = [AWS_EAST_STORAGE, AWS_WEST_STORAGE, AZURE_STORAGE_1,
                            AZURE_STORAGE_2, GOOGLE_EAST_STORAGE, GOOGLE_WEST_STORAGE]

    RETENTION_PERIOD_DAY = 86400
    RETENTION_PERIOD_MONTH = 2678400
    RETENTION_PERIOD_MAX = 3155760000

    TEST_FILE_PATH = os.path.join('integration_tests', 'test_files')

    DEFAULT_EXPIRES_IN_SECONDS = 10

    date_fmt = "%Y-%m-%dT%H:%M:%S.%fZ"

    LARGE_ENTITY_COUNT = 10
    HOST = 'http://localhost:5000'
    ADMIN_KEY = 'b7kNAC4xoe3QiAnLkplIjmfL3II+OX5EYHNxbwSuy7s='
    ADMIN_NAME = 'admin'

    def init_hiarc_config_admin(self):
        configuration = hiarc.Configuration()
        configuration.host = self.HOST
        configuration.api_key['Authorization'] = None
        configuration.api_key['X-Hiarc-Api-Key'] = self.ADMIN_KEY
        return configuration

    def init_hiarc_client_jwt_token(self, token):
        configuration = hiarc.Configuration()
        configuration.host = self.HOST
        configuration.api_key['X-Hiarc-Api-Key'] = None
        configuration.api_key['Authorization'] = token
        # ac = hiarc.ApiClient(configuration=configuration,
        #                      header_name='Authorization', header_value=f'Bearer {token}')
        return configuration

    def create_user(self, metadata=None):
        key = self.generate_key('user', 'user')
        return hiarc.CreateUserRequest(key=key, name=f'{self.get_punk_name()}-{key}', description='This user was kissed by a rose on the grey.', metadata=metadata)

    def create_file(self, metadata=None, extension='txt', storage=None):
        key = self.generate_key('file', 'file')
        return hiarc.CreateFileRequest(key=key, name=f'{self.get_punk_song()}.{extension}', description='This file redacted by Carl Grimm.', metadata=metadata, storage_service=storage)

    def create_file_copy(self, storage=None):
        key = self.generate_key('file', 'file')
        return hiarc.CopyFileRequest(key=key, storage_service=storage)

    def create_collection(self, metadata=None):
        key = self.generate_key('collection', 'collection')
        return hiarc.CreateCollectionRequest(key=key, name=f'{self.get_punk_albums()}-{key}', description='This collection is a Bjork cover band.', metadata=metadata)

    def create_classification(self, metadata=None):
        key = self.generate_key('classification', 'classification')
        return hiarc.CreateClassificationRequest(key=key, name=f'{self.get_punk_classifications()}-{key}', description='This classification karaokes 4 Non Blondes.', metadata=metadata)

    def create_legal_hold(self, metadata=None):
        key = self.generate_key('legal_hold', 'legal_hold')
        return hiarc.CreateLegalHoldRequest(key=key, name=f'legalhold-{key}', description='This legal hold paints house boats.', metadata=metadata)

    def create_retention_policy(self, seconds, metadata=None):
        key = self.generate_key('retention_policy', 'retention_policy')
        return hiarc.CreateRetentionPolicyRequest(key=key, seconds=seconds, name=f'retention-policy-{key}', description='This retention policy owns a biergarten.', metadata=metadata)

    def create_group(self, metadata=None):
        key = self.generate_key('group', 'group')
        return hiarc.CreateGroupRequest(key=key, name=f'{self.get_punk_group()}-{key}', description='This group loves John Barber', metadata=metadata)

    def increment_counter(self, counter_type):
        x = getattr(self, counter_type)
        x += 1
        setattr(self, counter_type, x)
        return x

    def generate_key(self, match, prefix):
        return {
            'file': f"{prefix}-{self.increment_counter('curr_file')}",
            'collection': f"{prefix}-{self.increment_counter('curr_coll')}",
            'user': f"{prefix}-{self.increment_counter('curr_user')}",
            'group': f"{prefix}-{self.increment_counter('curr_group')}",
            'retention_policy': f"{prefix}-{self.increment_counter('curr_retention_policy')}",
            'legal_hold': f"{prefix}-{self.increment_counter('curr_legal_hold')}",
            'classification': f"{prefix}-{self.increment_counter('curr_classification')}",
            'unique': f"{prefix}-{str(uuid.uuid4())}"
        }[match]

    def compare_dict_to_entity(self, e1, e2):
        return e1['key'] == e2.key and e1['name'] == e2.name and e1['description'] == e2.description and e1['metadata'] == e2.metadata

    def compare_entity_to_entity(self, e1, e2):
        return e1.key == e2.key and e1.name == e2.name and e1.description == e2.description and e1.metadata == e2.metadata

    def get_test_metadata(self):
        return {
            "department": "sales",
            "quotaCarrying": True,
            "targetRate": 4.234,
            "level": 3,
            "startDate": dateutil.parser.parse("2020-02-29T22:33:50.134Z")
        }

    def get_punk_name(self):
        punk_names = ['Elivs Costello', 'Debbie Harry', 'David Byrne',
                      'Siouxsie Sioux', 'Vicki Peterson', 'Mark Mothersbaugh',
                      'Josh Freese', 'Dave Quackenbush', 'Paul Westerberg',
                      'Exene Cervenka', 'Jello Biafra', 'Chris Hannah', 'Kim Deal']
        return choice(punk_names)

    def get_punk_group(self):
        punk_groups = ['The Attractions', 'Blondie', 'Talking Heads',
                       'The Banshees', 'The Bangles', 'Devo',
                       'The Vandals', 'The Replacements',
                       'X', 'Dead Kennedys', 'Propagandhi', 'Pixies']
        return choice(punk_groups)

    def get_punk_classifications(self):
        punk_classifications = ['Power Pop', 'New Wave', 'Punk',
                                'Ska', 'Hardcore', 'Emo',
                                'Skate Punk', 'Post Punk',
                                'Screamo', 'Grindcore', 'Riot Grrl', 'Pop Punk']
        return choice(punk_classifications)

    def get_punk_song(self):
        punk_songs = ['No Action', 'Heart of Glass', 'Burning Down the House',
                      'Cities in Dust', 'Walk like an Egyptian', 'Uncontrollable Urge',
                      'Eurobarge', 'Can\\\'t Hardly Wait',
                      'Los Angeles', 'Police Truck', 'Ska Sucks', 'Debaser']
        return choice(punk_songs)

    def get_punk_albums(self):
        punk_albums = ['This Year\\\'s Model', 'Parallel Lines', 'More Songs about Buildings and Food',
                       'The Scream', 'Different Light', 'Q: Are We Not Men? A: We are Devo!',
                       'Hitler Bad, Vandals Good', 'Pleased to Meet Me',
                       'Los Angeles', 'Fresh Fruit for Rotting Vegetables', 'Today\\\'s Empires, Tomorrow\\\'s Ashes',
                       'Surfer Rosa']
        return choice(punk_albums)
