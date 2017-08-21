# import _thread as thread
# from time import sleep
#
#
# def fun(name):
#     cnt = 0
#     while True:
#         cnt += 1
#         print('thread_id: {0}, thread_name: {1},cnt: {2}'.format(thread.get_ident(), name, cnt))
#
# if __name__ == '__main__':
#     thread.start_new_thread(fun, ('first', ))
#     thread.start_new_thread(fun, ('second',))
#
#     sleep(2)
#
#################################
# """
# для ожидания завершения дочерних потоков главный поток засыпает на 6 сек
# """
# import _thread as thread
# import time
#
#
# def counter(id, count):
#     for i in range(count):
#         time.sleep(1)
#
#         mutex.acquire()
#         print('[{0}] => {1}'.format(id, i))
#         mutex.release()
#
# mutex = thread.allocate_lock()
# for i in range(5):
#     thread.start_new_thread(counter, (i, 5))
#
# time.sleep(6)
# print('Main thread exiting.')
###########################################

# """
# для ожидания завершения дочерних потоков главный поток через проверку
# """
# import _thread as thread
# import time
#
# cnt_th = 10
# stdout_mutex = thread.allocate_lock()
# exit_mutex = [False] * cnt_th
#
#
# def counter(id, count):
#     for i in range(count):
#         #time.sleep(1)
#
#         stdout_mutex.acquire()
#         print('[{0}] => {1}'.format(id, i))
#         stdout_mutex.release()
#     exit_mutex[id] = True
#
#
# for i in range(cnt_th):
#     thread.start_new_thread(counter, (i, 100))
#
# while False in exit_mutex:
#     time.sleep(0.25)
#
# print('Main thread exiting.')
#
