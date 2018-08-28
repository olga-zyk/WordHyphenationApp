from src.hyphenator.hyphenation_alg import Hyphenator
from src.utils.timer import Timer


def time_measurement(hyp, ret_array, timer, word_list):
    timer.start()
    ret = [hyp.hyphenate(word) for word in word_list]
    timer.stop()
    if ret_array:
        return timer.duration(), ret
    else:
        return timer.duration(), None


def test_optimized(word_list, ret_array=False):
    hyp = Hyphenator({'search': Hyphenator.SEARCH_OPTIMIZED})
    timer = Timer()

    return time_measurement(hyp, ret_array, timer, word_list)


def test_old(word_list, ret_array=False):
    hyp = Hyphenator({'search': Hyphenator.SEARCH_LINEAR})
    timer = Timer()

    return time_measurement(hyp, ret_array, timer, word_list)


word_file = r'C:\Users\dev\Desktop\google-10000-english-usa-no-swears-long.txt'
test_count = 1
compare_hyp_results = False

with open(word_file, mode='r') as file:
    words = [line.strip() for line in file.readlines()]

results_old = [test_old(words, compare_hyp_results) for i in range(test_count)]
dur_old = [dur for (dur, w_ret) in results_old]
dur_old_avg = sum(dur_old) / len(dur_old)
print('old (avg, seconds): {dur:.4f}'.format(dur=dur_old_avg))

results_opt = [test_optimized(words, compare_hyp_results) for i in range(test_count)]
dur_opt = [dur for (dur, w_ret) in results_opt]
dur_opt_avg = sum(dur_opt) / len(dur_opt)
print('optimized (avg, seconds) {dur:.4f}'.format(dur=dur_opt_avg))

print('faster: {perc:.0%} ({mult:.2f}x)'.format(perc=(dur_old_avg - dur_opt_avg) / dur_old_avg,
                                                mult=dur_old_avg / dur_opt_avg))
if compare_hyp_results:
    a = [w_ret for (dur, w_ret) in results_old]
    b = [w_ret for (dur, w_ret) in results_opt]
    print('hyphenated results are equal:', a == b)
    if a != b:
        print(a, b)
