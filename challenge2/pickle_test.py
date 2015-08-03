student = {}
student['name'] = 'Jack'
student['course'] = 'Urban Skills Lab'
student['enrolled'] = True
student['misc'] = ('full-time', )

import pickle
try:
    with open('test_pickle.pkl', 'wb') as f:
        pickle.dump(student, f)
except IOError, e:
    print 'IOError: ',e